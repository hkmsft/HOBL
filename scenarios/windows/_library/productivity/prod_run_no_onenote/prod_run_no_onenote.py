# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import scenarios.app_scenario
from parameters import Params
import logging
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import utilities.call_rpc as rpc
from . import default_params

# Description:
#   Run productivity apps (no OneNote)

class ProdRunNoOnenote(scenarios.app_scenario.Scenario):
    # Set default parameters:
    default_params.run()

    actions = None

    def setUp(self):
        # Load InputInject plugin
        result = rpc.plugin_load(self.dut_ip, self.rpc_port, "InputInject", "InputInject.Application", "C:\\hobl_bin\\InputInject\\InputInject.dll")

        # Load actions JSON.
        actions_json = os.path.join(os.path.dirname(__file__), "prod_run_no_onenote.json")
        self.actions = self.load_action_json(actions_json)

        # Execute Setup actions, if they exist
        setup_action = self._find_next_type("Setup", json=self.actions)
        if setup_action:
            self.run_actions(setup_action["children"])

    def runTest(self):
        # Execute Run Test actions.
        run_action = self._find_next_type("Run Test", json=self.actions)
        if run_action:
            self.run_actions(run_action["children"])
        else:
            # No "Run Test" action in actions JSON, so execute all actions.
            self.run_actions(self.actions)

    def tearDown(self):
        # Execute Teardown actions, if they exist
        teardown_action = self._find_next_type("Teardown", json=self.actions)
        if teardown_action:
            self.run_actions(teardown_action["children"])
