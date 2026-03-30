# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

##
# sleep_wake
# 
# Wake up or sleep the device
# Intended to be used manually or through wait for dut communication
#
# Setup instructions:
#   Specify the command to wake up or sleep the device with the "sleep_wake_call" parameter in your parameters file.
##

import logging
import core.app_scenario
from core.parameters import Params


class SleepWake(core.app_scenario.Scenario):
    module = __module__.split('.')[-1]

    # Override collection of config data, traces, and execution of callbacks
    
    # Prevent any tools from running
    Params.setOverride('global', 'prep_tools', '')

    # Get parameters
    sleep_wake_call = Params.get('global', 'sleep_wake_call')

    is_prep = True

    def setUp(self):
        # Don't call base setUp so that we don't interact with DUT.
        return

    def runTest(self):    
        if self.sleep_wake_call != '':      
            self._host_call(self.sleep_wake_call)            
            logging.info("DUT power toggled.")

    def tearDown(self):
        # Don't call base tearDown so that we don't interact with DUT.
        return

    def kill(self):
        # Prevent base kill routine from running
        return 0
