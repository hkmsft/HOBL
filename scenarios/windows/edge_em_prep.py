# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

# Environment set up for the Browser Efficiency Test

import builtins
import logging
import core.app_scenario
from core.parameters import Params
import time

class EdgeEMPrep(core.app_scenario.Scenario):
    module = __module__.split('.')[-1]

    # Set default parameters
    Params.setDefault(module, 'efficiency_mode', 'default') 

    Params.setOverride("global", "prep_tools", "")
    is_prep = True
    efficiency_mode = Params.get(module, 'efficiency_mode')

    # Variables
    success = False

    def runTest(self):       
        # Set reg key to disable Efficiency Mode
        self._call(["cmd.exe", '/C reg delete "HKLM\\Software\\Policies\\Microsoft\\Edge\\EfficiencyModeEnabled" /f'], expected_exit_code="")
        self._call(["cmd.exe", '/C reg delete "HKLM\\Software\\Policies\\Microsoft\\Edge\\EfficiencyMode" /f'], expected_exit_code="")
        time.sleep(10)
        
        if self.efficiency_mode == 'disabled': #disable
            self._call(["cmd.exe", '/C reg add "HKLM\\Software\\Policies\\Microsoft\\Edge" /v EfficiencyModeEnabled /t REG_DWORD /d 0 /f'])
        elif self.efficiency_mode == 'maximum': #max
            # self._call(["cmd.exe", '/C reg add "HKLM\\Software\\Policies\\Microsoft\\Edge" /v EfficiencyModeEnabled /t REG_DWORD /d 1 /f'])
            self._call(["cmd.exe", '/C reg add "HKLM\\Software\\Policies\\Microsoft\\Edge" /v EfficiencyMode /t REG_DWORD /d 5 /f'])
        elif self.efficiency_mode == 'balanced': #balanced
            self._call(["cmd.exe", '/C reg add "HKLM\\Software\\Policies\\Microsoft\\Edge" /v EfficiencyModeEnabled /t REG_DWORD /d 1 /f'])
            self._call(["cmd.exe", '/C reg add "HKLM\\Software\\Policies\\Microsoft\\Edge" /v EfficiencyMode /t REG_DWORD /d 4 /f'])
        
        time.sleep(5)
        self.success = True

    def tearDown(self):
        if self.success:
            self.createPrepStatusControlFile()
        core.app_scenario.Scenario.tearDown(self)
