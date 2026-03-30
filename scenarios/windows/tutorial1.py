# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import core.app_scenario
from core.parameters import Params
import logging
import time

# Tutorial for creating a scenario:
#   - Print "Hello World" to log and delay

class HelloWorld(core.app_scenario.Scenario):
    # Set default parameters
    Params.setDefault('tutorial1', 'duration', '1')  # Seconds

    # Get parameter values
    duration = Params.get('tutorial1', 'duration')

    def runTest(self):
        logging.info("Hello World")
        time.sleep(int(self.duration))
    

