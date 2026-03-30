# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

##
# Hard reboot
# 
# Hard reboots the device
# Intended to be used manually or through wait for dut communication
#
# Setup instructions:
#   Specify the command to hard reboot the device with the "hard_reboot_call" parameter in your parameters file.
##

import logging
import core.app_scenario
from core.parameters import Params
import time


class HardReboot(core.app_scenario.Scenario):
    module = __module__.split('.')[-1]

    # Override collection of config data, traces, and execution of callbacks 
    
    # Prevent any tools from running
    Params.setOverride('global', 'prep_tools', '')

    # Get parameters
    hard_reboot_call = Params.get('global', 'hard_reboot_call')

    is_prep = True

    def setUp(self):
        # Don't call base setUp so that we don't interact with DUT.
        return

    def runTest(self):    
        if self.hard_reboot_call != '':      
            self._host_call(self.hard_reboot_call)            
            logging.info("DUT will be getting hard rebooted.")
            time.sleep(15)
            self._wait_for_dut_comm()

    def tearDown(self):
        # Don't call base tearDown so that we don't interact with DUT.
        return

    def kill(self):
        # Prevent base kill routine from running
        return 0
