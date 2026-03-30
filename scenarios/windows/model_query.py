# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import core.app_scenario
from core.parameters import Params
import logging
import time

# Tutorial for creating a scenario:
#   - Execute shell command on DUT

class ModelQuery(core.app_scenario.Scenario):
    # Set default parameters

    # Get parameter values

    is_prep = True

    def setUp(self):
        # Don't call base setUp so that we don't interact with DUT.
        return

    def runTest(self):
        result = self._call(['powershell.exe', r'(gwmi win32_ComputerSystem).Model'])
        logging.info("Result: " + result)
    
    def tearDown(self):
        # Don't call base tearDown so that we don't interact with DUT.
        return

    def kill(self):
        # Prevent base kill routine from running
        return 0

