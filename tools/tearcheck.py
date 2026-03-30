# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging
import os
import sys
import threading
import time

from core.parameters import Params
from core.app_scenario import Scenario


class Tool(Scenario):
    '''
    Check stdin for 'teardown' and end test when consumed
    '''
    module = __module__.split('.')[-1]

    tearEvt = threading.Event()

    def initCallback(self, scenario):
        # Initialization code
        # Keep a pointer to the scenario that this tools is being run with
        self.scenario = scenario
        self.scenario.enable_tool_threading = True

        self.thread = StdinListenerThread(self.tearEvt)

    def testBeginCallback(self):
        self.thread.start()

    def toolStatusCallback(self):
        if self.tearEvt.is_set():
            return (1, "end test")
        return (0, "continue test")

class StdinListenerThread(threading.Thread):
    def __init__(self, tearEvt):
        super().__init__()
        self.tearEvt = tearEvt

    def run(self):
        for line in sys.stdin:
            if line.strip().lower() == "teardown":
                logging.info("Teardown input received. Ending test")
                self.tearEvt.set()
                break
