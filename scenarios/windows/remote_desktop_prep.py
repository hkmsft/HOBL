# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

#Environment set up for the Bowser Efficiency Test

import builtins
import os
import logging
import core.app_scenario
from core.parameters import Params

class RemoteDesktopPrep(core.app_scenario.Scenario):
    module = __module__.split('.')[-1]
    # Override collection of config data, traces, and execution of callbacks 
    # Params.setOverride("global", "collection_enabled", "0")
    is_prep = True

    def runTest(self):       
        # Set reg keys to enable remote desktop client
        logging.info('Setting reg keys.')
        self._call(["cmd.exe", '/C reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f'])
        self._call(["cmd.exe", '/C netsh adv firewall set rule group=@FirewallAPI.dll,-28752 new enable=yes'])
        self._call(["cmd.exe", '/C reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon" /v ForceAutoLogon /t REG_DWORD /d 0x0 /f'])
        
    def tearDown(self):
        core.app_scenario.Scenario.tearDown(self)
