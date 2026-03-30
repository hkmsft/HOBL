# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import builtins
import logging
import core.app_scenario
import time, os
from core.parameters import Params

class Transfer8g(core.app_scenario.Scenario):
    module = __module__.split('.')[-1]
    # Set default parameters

    # Local parameters
    prep_scenarios = ["diskspd_prep"]

        
    def setUp(self):
        #Set test tool and file
        self.diskspd_tool = self.dut_exec_path + "\\diskspeed_resources\\diskspd.exe"
        self.dut_test_file1 = self.dut_exec_path + "\\diskspeed_resources\\8G.tmp"
        self.dut_local_copy_path = "c:\\temp\\copy_test"

        # Deleting test file from test dir and purging from the recycle bin
        logging.info("Deleting previous test files from DUT.")
        self._call(["cmd.exe", "/C rmdir /s /q " + self.dut_local_copy_path + " >nul 2>&1"])
        logging.info("Creating copy_test directory.")
        self._call(["cmd.exe", "/C mkdir " + self.dut_local_copy_path])
        core.app_scenario.Scenario.setUp(self)
        
    def runTest(self):
        # Copying Test file to test directory
        logging.info("Copying 8G.tmp file to \\copy_test directory.")
        self._call(["cmd.exe", "/C copy " + self.dut_test_file1 + " " + self.dut_local_copy_path + "\\8G.tmp"])
