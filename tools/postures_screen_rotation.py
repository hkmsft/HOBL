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


class Tool(Scenario):
    '''
    Deprecated.
    '''
    module = __module__.split('.')[-1]

    # Set default parameters
    Params.setDefault(module, 'posture_code', '5')
    #Params.setDefault(module, 'mute', "False")

    # Get parameters
    posture_code = Params.get(module, 'posture_code')
    rotation_code = Params.get(module, 'rotation_code')
    platform = Params.get('global', 'platform')
    screem_rotation = Params.get('global', 'screen_roation')
    #mute = Params.get(module, 'mute')

    def initCallback(self, scenario):

        self.scenario = scenario

        
        if self.platform.lower() == "android":
            
            # Use adb command to set postures from 0-15

            # Set Rotation

            if screen_rotation:

                logging.info("Set screen rotation")

                self._host_call("adb -s " + self.dut_ip + ":5555 shell settings put system accelerometer_rotation 0", expected_exit_code="")
                self._host_call("adb -s " + self.dut_ip + ":5555 shell settings put system user_rotation 1", expected_exit_code="")
            
            logging.info("Setting posture code to: " + self.posture_code)

            self._host_call("adb -s " + self.dut_ip + ":5555 shell am start -n com.pst.posturetool/.MainActivity -e posture " + self.posture_code + " -es rotation 0")
            time.sleep(5)

        return

    def testBeginCallback(self):
        pass

    def testEndCallback(self):
        pass

    def dataReadyCallback(self):
        pass




