# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

##
# Disable adaptive color
##

import time
import logging
from core.parameters import Params


import core.app_scenario


class AdaptiveColorDisable(core.app_scenario.Scenario):
    module = __module__.split('.')[-1]

    # Parameter for enable or disable recall
    Params.setDefault(module, 'recall_mode', '1')


    # Get Parameter
    recall_mode = Params.get(module, 'recall_mode')

    is_prep = True


    def runTest(self):
        logging.info("Launching WinAppDriver.exe on DUT")

        self._call([
            (self.dut_exec_path + "\\WindowsApplicationDriver\\WinAppDriver.exe"),
            (self.dut_resolved_ip + " " + self.app_port)],
            blocking=False
        )

        desired_caps = {}
        desired_caps["app"] = "Root"

        self.driver = self._launchApp(desired_caps)

        self._call(["cmd.exe", '/C start ms-settings:privacy'])
        time.sleep(1)

        # Go to recall & snapshots setting
        try:
            logging.info("trying to open recall settings")
            self.driver.find_element_by_xpath('//*[contains(@Name, "Recall & snapshots")]').click()
            time.sleep(3)
        except:
            logging.error("Couldn't find recall settings")
            self.driver.close()
            self.fail("Couldn't find recall settings. Ignore if recall is not supported on this device")

        toggle_switch = self.driver.find_element_by_xpath('//Button[contains(@Name, "Save snapshots")]')
        if self.recall_mode == "1":
            if not toggle_switch.is_selected():
                toggle_switch.click()
                logging.info("Recall enabled")
            else:
                logging.info("Recall already turned on")

        elif self.recall_mode == "0":
            if toggle_switch.is_selected():
                toggle_switch.click()
                logging.info("Recall disabled")
            else:
                logging.info("Recall already turned off")
        # self._page_source(self.driver)
        # try:
        #     toggle_switch = self.driver.find_element_by_xpath("//*[@Name = 'Adaptive color' and @ClassName = 'ToggleSwitch']")
        # except:
        #     logging.info("Adaptive color setting not found, exiting.")
        #     self.driver.close()
        #     time.sleep(1)
        #     self.createPrepStatusControlFile()
        #     return

        # if toggle_switch.is_selected():
        #     toggle_switch.click()
        #     logging.info(f"Adaptive color disabled")
        # else:
        #     logging.info(f"Adaptive color already disabled")

        time.sleep(1)

        self.driver.close()
        time.sleep(3)
        # self.createPrepStatusControlFile()


    def tearDown(self):
        core.app_scenario.Scenario.tearDown(self)

        logging.debug("Killing SystemSettings.exe")
        self._kill("SystemSettings")

        logging.debug("Killing WinAppDriver.exe")
        self._kill("WinAppDriver")


    def kill(self):
        try:
            logging.debug("Killing SystemSettings.exe")
            self._kill("SystemSettings.exe")
        except:
            pass

        try:
            logging.debug("Killing WinAppDriver.exe")
            self._kill("WinAppDriver.exe")
        except:
            pass
