# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import core.app_scenario
from core.parameters import Params


class ScenarioInvalid(core.app_scenario.Scenario):
    module = __module__.split('.')[-1]

    def setUp(self):
        # Don't call setUp so that we don't interact with DUT.
        error_msg = Params.getCalculated("scenario_invalid")
        self.error_fail(error_msg)

    def runTest(self):
        # Don't call runTest so that we don't interact with DUT.
        return

    def tearDown(self):
        # Don't call base tearDown so that we don't interact with DUT.
        return

    def kill(self):
        # Prevent base kill routine from running
        return 0
