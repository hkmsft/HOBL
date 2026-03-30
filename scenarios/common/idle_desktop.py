# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

##
# Idle at the Desktop
#
# Setup instructions:
#   None
##

import builtins
import logging
import time
import core.app_scenario
from core.parameters import Params


class IdleDesktop(core.app_scenario.Scenario):

    module = __module__.split('.')[-1]
    # Set default parameters
    Params.setDefault(module, 'duration', '1200')  # Seconds

    # Local parameters
    prep_scenarios = []

    def setUp(self):
        # Get parameters
        platform = Params.get('global', 'platform').lower()

        # minimize any windows
        if platform == 'windows':
            self._call(["powershell.exe", '-command "$x = New-Object -ComObject Shell.Application; $x.minimizeall()"'])
        core.app_scenario.Scenario.setUp(self)


    def runTest(self):
        # Get parameters
        duration = Params.get('idle_desktop', 'duration')

        # Sleep for specified duration
        logging.info("Sleeping for " + duration)
        time.sleep(float(duration))
        if self.enable_screenshot == '1':
            self._screenshot(name="end_screen.png")
