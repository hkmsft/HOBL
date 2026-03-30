# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

##
# Set refresh rate
##

import time
import logging

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from core.parameters import Params
import core.app_scenario


class RefreshRate(core.app_scenario.Scenario):
    module = __module__.split('.')[-1]

    # Set default parameters
    Params.setDefault(module, 'rate', '60') # Number or 'dynamic Number'
    Params.setDefault(module, 'display', 'default') # Number or 'default'

    # Get parameters
    rate = Params.get(module, 'rate')
    display = Params.get(module, 'display')

    is_prep = True

    def runTest(self):
        logging.info("Launching WinAppDriver.exe on DUT")

        self._call([
            (self.dut_exec_path + "\\WindowsApplicationDriver\\WinAppDriver.exe"),
            (self.dut_ip + " " + self.app_port)],
            blocking=False
        )

        desired_caps = {}
        desired_caps["app"] = "Root"

        self.driver = self._launchApp(desired_caps)

        self._call(["cmd.exe", '/C start ms-settings:'])
        time.sleep(1)

        self.driver.find_element_by_name("System").click()
        time.sleep(1)

        self.driver.find_element_by_name("Display").click()
        time.sleep(1)

        self.driver.find_element_by_name("Advanced display").click()
        time.sleep(1)

        if self.display != 'default':
            if not self.display.isdigit():
                raise Exception("display parameter is invalid")

            self.driver.find_element_by_xpath('//ComboBox[contains(@Name, "Select a display")]').click()
            time.sleep(1)

            target_display = self.driver.find_element_by_xpath(f'//*[contains(@Name, "Display {self.display}")]')
            time.sleep(1)

            if target_display.is_selected():
                logging.info(f"Target display {self.display} already selected")
            else:
                logging.info(f"Target display set to display {self.display}")

            target_display.click()
            time.sleep(1)

        self.driver.find_element_by_name("Refresh rate").click()
        time.sleep(1)

        if self.rate.isdigit():
            target_rate = self.driver.find_element_by_name(f"{self.rate} Hz")
        else:
            start_dynamic_rate = self.rate.split(" ")[-1]

            if not start_dynamic_rate.isdigit():
                raise Exception("rate parameter is invalid")

            target_rate = self.driver.find_element_by_xpath(
                f"//*[contains(@Name, 'Dynamic') and contains(@Name, {start_dynamic_rate})]"
            )

        time.sleep(1)

        if target_rate.is_selected():
            logging.info(f"Target rate {self.rate} already selected")
        else:
            target_rate.click()
            time.sleep(1)

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "Keep changes"))
            ).click()

            time.sleep(2)

            logging.info(f"Successfully set refresh rate to {self.rate}")

        self.driver.close()


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
