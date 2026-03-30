# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging
import os
import threading
import time

from core.parameters import Params
from core.app_scenario import Scenario


class Tool(Scenario):
    '''
    Run TTD (Time Travel Debugging)
    '''
    module = __module__.split('.')[-1]

    Params.setDefault(module, 'start',   '0', desc="Start time during test execution in seconds.")
    Params.setDefault(module, 'end',     '0', desc="End time during test execution in seconds.")
    Params.setDefault(module, 'process', '',  desc="Process to attach to.")

    delay   = int(Params.get(module, 'start'))
    dur     = max(int(Params.get(module, 'end')) - delay, 0)
    process = os.path.splitext(Params.get(module, 'process'))[0].lower()

    def initCallback(self, scenario):
        # Initialization code
        # Keep a pointer to the scenario that this tools is being run with
        self.scenario = scenario
        self.scenario.enable_tool_threading = True

        self.endEvent = threading.Event()

        self.out_dir = f"{scenario.dut_data_path}\\ttd"

        self.thread = TTDThread(self)

    def testBeginCallback(self):
        self.thread.start()

    def toolStatusCallback(self):
        if self.endEvent.is_set():
            return (1, "end test")
        return (0, "continue test")

class TTDThread(threading.Thread):
    def __init__(self, tool):
        super().__init__()
        self.tool = tool

    def run(self):
        if not self.tool.process:
            logging.error("No process specified")
            self.tool.endEvent.set()
            return

        logging.info(f"Delaying TTD by {self.tool.delay}s")
        time.sleep(self.tool.delay)

        result = self.tool.scenario._call(
            ["powershell.exe", f"(Get-Process | Where-Object {{ $_.ProcessName.ToLower().Equals('{self.tool.process}') }}).Id"],
            log_output=False
        ).splitlines()

        if len(result) != 1:
            logging.error(f"Expected one pid only, got {len(result)}. Cannot start TTD")
            self.tool.endEvent.set()
            return

        pid = int(result[0])

        self.tool.scenario._remote_make_dir(self.tool.out_dir)

        logging.info(f"Running TTD for {self.tool.dur}s")

        self.tool.scenario._call(
            ["tttracer.exe", f"-attach {pid} -timer {self.tool.dur} -tExit 0 -out {self.tool.out_dir}"]
        )

        logging.info(f"Stopped TTD")

        self.tool.endEvent.set()
