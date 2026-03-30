# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

##
# Netflix app
#
# Setup instructions:
#   Set video to 120s, sw does not set the time
##
from builtins import str
import builtins
import logging
import os
import time
import appium.common.exceptions as exceptions
from appium import webdriver
import core.app_scenario
import selenium.common.exceptions as exceptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from core.parameters import Params
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Netflix_app(core.app_scenario.Scenario):
    module = __module__.split('.')[-1]
   
    # Set default parameters
    Params.setDefault(module, 'duration', '1200')
    Params.setDefault(module, 'title', 'A Series of Unfortunate Events')  # Just has to be unique substring of title

    # Get parameters
    duration = Params.get(module, 'duration')
    title = Params.get(module, 'title')

    # Local parameters
    prep_scenarios = ["netflixapp_prep"]


    def setUp(self):
        logging.info("Launching WinappDriver.exe on DUT.")
        self._call([(self.dut_exec_path + "\\WindowsApplicationDriver\\WinAppDriver.exe"), (self.dut_resolved_ip + " " + self.app_port)], blocking=False)
        time.sleep(1)
        desired_caps = {}
        desired_caps["app"] = "4DF9E0F8.Netflix_mcm4njqhnhss8!Netflix.App"
        self.driver = self._launchApp(desired_caps)
        time.sleep(5)
        self._page_source(self.driver)

        # Search for video
        self.driver.find_element_by_xpath('//*[contains(@Name,"Search")]').click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(self.title + Keys.RETURN).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[contains(@Name,"' + self.title + '")]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[contains(@Name,"Play")]').click()
        time.sleep(10)
        core.app_scenario.Scenario.setUp(self)

    def runTest(self):
        # Maximize window
        self.driver.maximize_window()
        time.sleep(1)
        ActionChains(self.driver).move_by_offset(-50, -50).perform()
        fullscreen = self.driver.find_element_by_name("Fullscreen")
        fullscreen.click()
        logging.info("Sleeping for " + str(self.duration) + " seconds")
        time.sleep(int(self.duration))    

        # Closing Netflix app
        self.driver.close()
        if self.enable_screenshot == '1':
            self._screenshot(name="end_screen.png")
       

    def tearDown(self):
        logging.info("Performing teardown.")
        core.app_scenario.Scenario.tearDown(self)
        time.sleep(2)
        self._kill("WinAppDriver.exe")   