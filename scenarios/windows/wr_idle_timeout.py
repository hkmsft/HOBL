# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

##
# web_replay idle timeout
##

import core.app_scenario
from core.parameters import Params


class WebReplayIdleTimeout(core.app_scenario.Scenario):
    module = __module__.split('.')[-1]


    def setUp(self):
        self._web_replay_idle_timeout()
        return

    def runTest(self):
        # Don't call runTest so that we don't interact with DUT
        return

    def tearDown(self):
        # Don't call base tearDown so that we don't interact with DUT
        return

    def kill(self):
        # Prevent base kill routine from running
        return 0
