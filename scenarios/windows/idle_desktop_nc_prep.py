# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

##
# Prep for Idle desktop with wifi not connected
# 
# Setup instructions:
##

import builtins
import os
import logging
import core.app_scenario
from core.parameters import Params
import time


class CsFloorPrep(core.app_scenario.Scenario):
    module = __module__.split('.')[-1]
    # Set default parameters

    # Get parameters

    # Override collection of config data, traces, and execution of callbacks 
    # Params.setOverride("global", "collection_enabled", "0")
    is_prep = True

    def runTest(self):
        # self._upload("scenarios\\idle_desktop_nc_resources", self.dut_exec_path)
        self._upload("scenarios\\windows\\idle_desktop_nc\\idle_desktop_nc_wrapper.cmd", os.path.join(self.dut_exec_path, "idle_desktop_nc_resources"))
        self._upload("utilities\\proprietary\\sleep\\sleep.exe", os.path.join(self.dut_exec_path, "sleep"))

    def tearDown(self):
        self.createPrepStatusControlFile()
        core.app_scenario.Scenario.tearDown(self)
