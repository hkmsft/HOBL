# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from functools import partial
import os
from core.parameters import Params
import utilities.open_source.modules

import_run_user_only = partial(utilities.open_source.modules.import_run_user_only, here=__file__)

def run():
    Params.setCalculated('scenario_section', __package__.split('.')[-1])
    run_user_only()
    return

def run_user_only():
    import_run_user_only('..\\teams_collect_call_health')
    import_run_user_only('..\\teams_stop_screenshare')
    Params.setUserDefault('teams', 'access_key', '-1', desc='The access key for the Teams Bots Server. Contact HOBL Support to inquire for a key.', valOptions=[])
    Params.setUserDefault('teams', 'send_screen', '0', desc='Set to 1 to have the DUT share its screen in the meeting.', valOptions=['0', '1'])
    Params.setUserDefault('teams', 'collect_call_health', '1', desc='Set to 1 to have the call health data collected.', valOptions=['0', '1'])
    return
