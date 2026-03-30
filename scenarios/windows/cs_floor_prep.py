# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

##
# Prep for Local Video Playback
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

    Params.setOverride("global", "prep_tools", "")

    is_prep = True

    def runTest(self):
        #self._upload('scenarios\\cs_floor_resources', self.dut_exec_path, check_modified=True)
        self._upload("scenarios\\windows\\cs_floor\\cs_floor_wrapper.cmd", os.path.join(self.dut_exec_path, "cs_floor_resources"))
        self._upload("utilities\\proprietary\\sleep\\sleep.exe", os.path.join(self.dut_exec_path, "sleep"))

        self.createPrepStatusControlFile()

    def tearDown(self):
        core.app_scenario.Scenario.tearDown(self)
