# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import builtins
import logging
import core.app_scenario
import time
from core.parameters import Params

class DiskspdPrep(core.app_scenario.Scenario):
    
    module = __module__.split('.')[-1]
    # Override collection of config data, traces, and execution of callbacks 
    # Params.setOverride("global", "collection_enabled", "0")
    is_prep = True

    def runTest(self):
        #Set test tool and file
        diskspd_tool = self.dut_exec_path + "\\diskspeed_resources\\diskspd.exe"
        dut_test_file1 = self.dut_exec_path + "\\diskspeed_resources\\8G.tmp"
        #dut_test_file2 = self.dut_exec_path + "\\diskspeed_resources\\1G.tmp"
        dut_test_seq = self.dut_exec_path + "\\diskspeed_resources\\1Gseq.tmp"
        dut_test_rand = self.dut_exec_path + "\\diskspeed_resources\\1Grand.tmp"

        # Copy over resources
        logging.info("Uploading Diskspd tools from hobl_bin\\scenarios\\diskspeed_resources to " + self.dut_exec_path)
        self._upload("utilities\\third_party\\diskspd.exe", self.dut_exec_path + "\\diskspeed_resources")

        # Generating the Test files to copy
        logging.info("Diskspd is generating 8GB test file.")
        self._call(["cmd.exe", "/C " + diskspd_tool + " -c8G " + dut_test_file1])
        logging.info("8G.tmp has been generated.")

        logging.info("Diskspd is generating 1GB sequential test file.")
        self._call(["cmd.exe", "/C " + diskspd_tool + " -b128k -o32 -t1 -W0 -s -S -w100 -c1G " + dut_test_seq])
        logging.info("1Gseq.tmp has been generated.")

        logging.info("Diskspd is generating 1GB random test file.")
        self._call(["cmd.exe", "/C " + diskspd_tool + " -b128k -o32 -t1 -W0 -r -S -w100 -c1G " + dut_test_rand])
        logging.info("1Grand.tmp has been generated.")

    def tearDown(self):
        self.createPrepStatusControlFile()
        logging.info("Performing teardown.")
        core.app_scenario.Scenario.tearDown(self)
        time.sleep(2)
        self._kill("WinAppDriver.exe")