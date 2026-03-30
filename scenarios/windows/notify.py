# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

##
# Send plan completion email
##

import core.app_scenario
from core.parameters import Params

from utilities.open_source.email_notify import send_plan_complete_email


class Notify(core.app_scenario.Scenario):
    module = __module__.split('.')[-1]

    is_prep = True

    Params.setOverride('global', 'local_execution',    '1')
    Params.setOverride('global', 'post_run_delay', '0')

    Params.setDefault(module, 'plan_run_type', '')

    plan_run_type = Params.get(module, 'plan_run_type')


    def setUp(self):
        # Don't call base setUp so that we don't interact with DUT
        return


    def runTest(self):
        send_plan_complete_email(self.plan_run_type)


    def tearDown(self):
        # Don't call base tearDown so that we don't interact with DUT
        return


    def kill(self):
        # Prevent base kill routine from running
        return 0
