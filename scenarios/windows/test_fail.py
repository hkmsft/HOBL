# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import core.app_scenario
from core.parameters import Params
import os
import core.call_rpc as rpc
import time
import logging

# Tutorial for creating a scenario:
#   - Execute shell command on DUT

class Test(core.app_scenario.Scenario):

    def setUp(self):
        pass

    def runTest(self):
        self._call([
            (self.dut_exec_path + "\\WindowsApplicationDriver\\WinAppDriver.exe"),
            (self.dut_resolved_ip + " " + self.app_port)],
            blocking=False
        )
        desired_caps = {}
        desired_caps["app"] = "Root"
        self.driver = self._launchApp(desired_caps)
        # Force a failure by trying to find an element that doesn't exist
        self.driver.find_element_by_name("NON_EXISTING_ELEMENT")
        self.driver.close()

    def tearDown(self):
        self._kill("WinAppDriver.exe")

    def kill(self):
        self._kill("WinAppDriver.exe")
