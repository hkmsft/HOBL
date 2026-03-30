# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

##
# Idle at the Desktop in airplane mode
#
# Setup instructions:
#   None
##

from builtins import str
import builtins
import logging
import os
import time
import core.app_scenario
from core.parameters import Params


class IdleDesktopApm(core.app_scenario.Scenario):

    module = __module__.split('.')[-1]
    # Set default parameters
    Params.setDefault(module, 'duration', '300')  # Seconds
    Params.setDefault(module, 'airplane_mode', '1')
    Params.setDefault(module, 'radio_enable', '1')

    # Get parameters
    duration = Params.get(module, 'duration')
    platform = Params.get('global', 'platform')
    airplane_mode = Params.get(module, 'airplane_mode')
    radio_enable = Params.get(module, 'radio_enable')

     # Local parameters
    prep_scenarios = ["button_install", "lvp_prep"]

    airplane_enabled_duration = int(duration) + 30

    def setUp(self):
        core.app_scenario.Scenario.setUp(self, callback_test_begin="")

        # minimize any windows
        # if self.platform == 'Windows':
        #     self._call(["powershell.exe", '-command "$x = New-Object -ComObject Shell.Application; $x.minimizeall()"'])

        # Set airplane mode enable
        if self.airplane_mode == '1':
            try:
                # Set up 2nd config -Prerun command string for lvp_wrapper.cmd
                override_str = '[{\'Scenario\': \'' + self.module + '\'}]'
                config_str = os.path.join(self.dut_exec_path, "config_check.ps1 -Prerun -LogFile " + self.dut_data_path, self.testname + "_ConfigPre") + " -OverrideString " + '\\\"' + override_str + '\\\""'
                logging.info("CONFIG_STR: " + config_str)
                logging.info("Enabling airplane mode for " + str(self.airplane_enabled_duration) + " seconds.")
                if self.radio_enable == '0':
                    logging.info("cmd.exe /C " + os.path.join(self.dut_exec_path + "\lvp_resources" + "\lvp_wrapper.cmd") + ' ' + str(self.airplane_enabled_duration) + ' ' + self.dut_exec_path + ' ' + "APM " + config_str)
                    self._call(["cmd.exe", "/C " + os.path.join(self.dut_exec_path + "\lvp_resources" + "\lvp_wrapper.cmd") + ' ' + str(self.airplane_enabled_duration) + ' ' + self.dut_exec_path + ' ' + "APM " + config_str], blocking = False) 
                else:
                    wrapper_cmd_path = os.path.join(self.dut_exec_path, "lvp_resources", "lvp_wrapper.cmd")
                    logging.info("cmd.exe /C " + wrapper_cmd_path + ' ' + str(self.airplane_enabled_duration) + ' ' + self.dut_exec_path + ' ' + "RadioEnable " + config_str)
                    self._call(["cmd.exe", "/C " + wrapper_cmd_path + ' ' + str(self.airplane_enabled_duration) + ' ' + self.dut_exec_path + ' ' + "RadioEnable " + config_str], blocking = False) 
            except:
                pass
        
        # Delay to let airplane mode enable
        time.sleep(10)
        # Start recording power
        self._callback(Params.get('global', 'callback_test_begin'))

    def runTest(self):
        # Idle in APM for specified duration
        logging.info("Sleeping for " + self.duration)
        time.sleep(float(self.duration))

    def tearDown(self):
        logging.info("Performing teardown.")
#        if self.enable_screenshot == '1':
#            self._screenshot(name="end_screen.png")

         # Stop recording power
        self._callback(Params.get('global', 'callback_test_end'))

        # Give time for Stop command to propagate
        time.sleep(5)

        if self.airplane_mode =='1':
            try:
                if self.radio_enable == '0':
                    logging.info("cmd.exe /C " + os.path.join(self.dut_exec_path, "lvp_resources\AirplaneMode.exe -Disable"))
                    self._call(["cmd.exe", "/C " + os.path.join(self.dut_exec_path, "lvp_resources", "AirplaneMode.exe") + " -Disable"], blocking = False) 
                else:
                    logging.info("cmd.exe /C " + os.path.join(self.dut_exec_path, "lvp_resources\RadioEnable.exe -Enable"))
                    self._call(["cmd.exe", "/C " + os.path.join(self.dut_exec_path, "lvp_resources", "radioenable.exe") + " -Enable"], blocking = False) 
            except:
                pass
        logging.info("Delaying for 60 seconds to make sure WiFi is back up.")
        time.sleep(60)

        if self.enable_screenshot == '1':
            self._screenshot(name="end_screen.png")

        # Allow plenty of time for wifi to come back up
        time.sleep(30)
        core.app_scenario.Scenario.tearDown(self, callback_test_end="")
