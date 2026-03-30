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
    Params.setParam(None, 'i', '1')
    return

def run_user_only():
    import_run_user_only('..\\add_vid2_first_eff')
    import_run_user_only('..\\add_vid3_first_eff')
    import_run_user_only('..\\add_vid4_first_eff')
    import_run_user_only('..\\add_vid5_first_eff')
    import_run_user_only('..\\add_vid6_first_eff')
    import_run_user_only('..\\add_vid7_first_eff')
    import_run_user_only('..\\add_vid8_first_eff')
    import_run_user_only('..\\next_clip')
    return
