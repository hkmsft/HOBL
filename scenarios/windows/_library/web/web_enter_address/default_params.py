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
    Params.setDefault('web_enter_address', 'web_site_address', 'about:blank', desc='', valOptions=[])
    Params.setDefault('web_enter_address', 'new_tab', '0', desc='', valOptions=['0', '1'])
    Params.setDefault('web_enter_address', 'web_site_load_time', '20', desc='', valOptions=[])
    Params.setDefault('web_enter_address', 'event_tag', '', desc='', valOptions=[])
    return

def run_user_only():
    import_run_user_only('..\\..\\misc\\etw_event_tag')
    return
