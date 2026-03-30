# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

##
# charge_on
# 
# Turns on the device charger.
# Intended to be included at the end of a test plan
#
# Setup instructions:
#   Specify the command to call to turn on the charger for the "charge_on_call" parameter in your parameters file.
##

import logging
import core.app_scenario
from core.parameters import Params


class ChargeOn(core.app_scenario.Scenario):
    module = __module__.split('.')[-1]

    # Override collection of config data, traces, and execution of callbacks 

    # Prevent any tools from running
    Params.setOverride('global', 'prep_tools', '')

    # Get parameters
    charge_on_call = Params.get('global', 'charge_on_call')

    is_prep = True

    def setUp(self):
        # Don't call base setUp so that we don't interact with DUT.
        return

    def runTest(self):    
        logging.info("Attempting to turn on charger...")
        if self.charge_on_call == '':      
            logging.warning("No charge_on_call specified.")             
        else:
            self._host_call(self.charge_on_call)            
            logging.info("Charger turned on.")
        if Params.get('global', 'local_execution') == '1':
            self._host_call('utilities\\MsgPrompt.exe -WaitForAC')
            logging.info("Charger plugged in.")

    def tearDown(self):
        # Don't call base tearDown so that we don't interact with DUT.
        return

    def kill(self):
        # Prevent base kill routine from running
        return 0
