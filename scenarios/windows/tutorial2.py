# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import core.app_scenario
from core.parameters import Params
import logging
import time

# Tutorial for creating a scenario:
#   - Execute shell command on DUT

class HelloWorld(core.app_scenario.Scenario):
    # Set default parameters
    Params.setDefault('tutorial2', 'duration', '1')  # Seconds

    # Get parameter values
    duration = Params.get('tutorial2', 'duration')

    def runTest(self):
        result = self._call(["cmd.exe", "/c echo Hello World"])
        logging.info("Result: " + result)
        time.sleep(int(self.duration))
    

