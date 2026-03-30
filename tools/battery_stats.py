# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

# Tool wrapper for audio control

from builtins import str
from builtins import *
from core.parameters import Params
from core.app_scenario import Scenario
import logging
import sys
import os
import decimal
import time


class Tool(Scenario):
    '''
    Deprecated.
    '''
    module = __module__.split('.')[-1]

    # Set default parameters
    #Params.setDefault(module, 'mute', "False")

    # Get parameters
    platform = Params.get('global', 'platform')
    result_dir = Params.get('global', 'result_dir')
    dut_ip = Params.get('global', 'dut_ip')
    #mute = Params.get(module, 'mute')

    def initCallback(self, scenario):

        # Enable full wake history

        if self.platform.lower() == "android":

            logging.info("Enable wake history and reset battery stats")

            self._host_call("adb -s " + self.dut_ip + ":5555 shell dumpsys batterystats --enable full-wake-history", expected_exit_code="")
            time.sleep(5)

            # Reset battery statistics

            self._host_call("adb -s " + self.dut_ip + ":5555 shell dumpsys batterystats --reset", expected_exit_code="")
            time.sleep(5)

        return

    def testBeginCallback(self):
        pass

    def testEndCallback(self):
        pass

    def dataReadyCallback(self):

        
        if self.platform.lower() == "android":
            
            # Use adb command to fetch batery stats
            
            logging.info("Saving battery stats to: " + self.result_dir)

            # Dump battery stats

            self._host_call("adb -s " + self.dut_ip + ":5555 shell dumpsys batterystats > " + self.result_dir + "\\batterystats.txt", expected_exit_code="")
            time.sleep(5)

        return




