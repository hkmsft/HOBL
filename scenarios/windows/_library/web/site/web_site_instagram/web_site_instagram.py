# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import core.app_scenario
from core.parameters import Params
import logging
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import core.call_rpc as rpc

# Description:
#   Automatically generated standard scenario.

class WebSiteInstagram(core.app_scenario.Scenario):
    # Set default parameters:
    Params.setDefault('web_site_instagram', 'duration', '1')

    # Get parameter values:
    duration = Params.get('web_site_instagram', 'duration')


    def setUp(self):
        result = rpc.plugin_load(self.dut_ip, self.rpc_port, "InputInject", "InputInject.Application", "C:\\hobl_bin\\InputInject\\InputInject.dll")
        # Load actions JSON.
        actions_json = os.path.join(os.path.dirname(__file__), "web_site_instagram.json")
        self.load_action_json(actions_json)

        # Call base class setUp() to dump config, call tool callbacks, and start measurment
        core.app_scenario.Scenario.setUp(self)


    def runTest(self):
        # Loop through actions in JSON file and process:
        while(1):
            result = self.get_next_action()
            if result == 0 or result == 1:
                # Reached end of action list
                break
            logging.info("Performing action: " + str(result["id"]) + " " + str(result["type"]) + " " + str(result["description"]))
            self.process_action(result)


    def tearDown(self):
        # Call base class tearDown() to stop measurment, copy back data from DUT, and call tool callbacks
        core.app_scenario.Scenario.tearDown(self)

        # Add any additional tear down code here:

    
    def kill(self):
        # In case of scenario failure or termination, kill any applications left open here:

        return