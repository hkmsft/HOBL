# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.
import builtins
import logging
import core.app_scenario
import time, os
from core.parameters import Params

class Write4krand(core.app_scenario.Scenario):
    module = __module__.split('.')[-1]
    # Set default parameters
    Params.setDefault(module, 'block', '4')  # Block size in (K/M/G)bytes
    Params.setDefault(module, 'duration', '300')  # Seconds
    Params.setDefault(module, 'threads', '4')
    Params.setDefault(module, 'delay', '0')  # Seconds
    Params.setDefault(module, 'write', '100')  # Percentage
        
    # Get parameters
    block = Params.get(module, 'block')
    duration = Params.get(module, 'duration')
    threads = Params.get(module, 'threads')
    delay = Params.get(module, 'delay')
    write = Params.get(module, 'write')

    # Local parameters
    prep_scenarios = ["diskspd_prep"]
    
    def setUp(self):
        #Set test tool and file
        self.diskspd_tool = self.dut_exec_path + "\\diskspeed_resources\\diskspd.exe"
        self.dut_test_rand = self.dut_exec_path + "\\diskspeed_resources\\1Grand.tmp"
        core.app_scenario.Scenario.setUp(self)
        
    def runTest(self):
        # Performing sequential write test for 5 min
        logging.info("Performing " + self.block + "K block random write test for " + self.duration + " seconds")
        diskspd_data = self._call(["cmd.exe", "/C " + self.diskspd_tool + " -b" + self.block + "K -d" + self.duration + " -t" + self.threads + " -W" + self.delay + " -w" + self.write + " -o32 -r -S " + self.dut_test_rand])
