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
    Params.setDefault('web_site_amazon_got', 'new_tab', '0', desc='', valOptions=['0', '1'])
    return

def run_user_only():
    import_run_user_only('..\\..\\..\\misc\\recording_phase_begin')
    import_run_user_only('..\\..\\..\\misc\\recording_phase_end')
    import_run_user_only('..\\..\\web_enter_address')
    return
