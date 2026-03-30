# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging
import core.app_scenario
from core.parameters import Params
import time

##
# Install virtual button.
# Used to put device to sleep and wake up.
##

class ButtonInstall(core.app_scenario.Scenario):
    module = __module__.split('.')[-1]
    # Set default parameters

    # Get parameters
    dut_architecture = Params.get('global', 'dut_architecture')

    # Override collection of config data, traces, and execution of callbacks 
    Params.setOverride("global", "prep_tools", "")
    is_prep = True

    def runTest(self):
        # Upload
        self._upload('utilities\\proprietary\\button\\'  + self.dut_architecture + "\\*", self.dut_exec_path + "\\button")
        # self._upload('utilities\\proprietary\\pwrtest\\'  + self.dut_architecture + "\\*", self.dut_exec_path + "\\pwrtest")

        time.sleep(1)
        # Remove any existing button
        self._call(['cmd.exe' , ' /C "cd /D ' + self.dut_exec_path + '\\button & .\\button.exe -u"'], expected_exit_code="")
        # Install this button
        self._call(['cmd.exe', ' /C "cd /D ' + self.dut_exec_path + '\\button & .\\button.exe -i"'])
        self.createPrepStatusControlFile()

