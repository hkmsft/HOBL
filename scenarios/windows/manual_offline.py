# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import builtins
import logging
import core.app_scenario
import time
from core.parameters import Params
import sys
from utilities.open_source.widgets import Widgets


class ManualOffline(core.app_scenario.Scenario):
    logging.info("Beginning manual test scenario.")
    module = __module__.split('.')[-1]
    # Set default parameters
    Params.setDefault(module, 'duration', '')  # Seconds
    Params.setDefault(module, 'delay', '')  # Seconds
    Params.setDefault(module, 'start_prompt', '1') # 1 waits for user input, 0 starts recording power immediately
    Params.setDefault(module, 'teardown_prompt', '1') # 1 waits for user input, 0 stops tools immediately

    # Get parameters
    duration = Params.get(module, 'duration')
    delay = Params.get(module, 'delay')
    start_prompt = Params.get(module, 'start_prompt')
    teardown_prompt = Params.get(module, 'teardown_prompt')

    widgets = Widgets()

    def setUp(self):
        # Assuming run_report is only tool.  Initialize it.
        self.toolCallBacks("initCallback")

        if self.delay != '': 
            logging.info("Delaying for " + self.delay + " seconds before starting power measurement.")
            time.sleep(float(self.delay))

        if self.start_prompt == "1":
            self.widgets.about("Start Recording", "Press enter to START recording...")

        # Start recording power    
        logging.info("Starting power record.")
        self._callback(Params.get('global', 'callback_test_begin'))

    def runTest(self):
        if self.duration == '':
            logging.info("Duration not specified, presenting STOP dialog.")
            self.widgets.about("Stop Recording", "Press enter to STOP recording...")
        else:
            # Sleep for specified duration
            logging.info("Recording for " + self.duration + " seconds.")
            time.sleep(float(self.duration))
    
    def tearDown(self):
        # Stop recording power
        logging.info("Stopping power record.")
        self._callback(Params.get('global', 'callback_test_end'))

        # Framework Data Ready Callback
        self._callback(Params.get('global', 'callback_data_ready'))

        # Tool Report Callback
        self.toolCallBacks("reportCallback", fail_pass=True)

    def kill(self):
        # prevent default kill()
        return 0