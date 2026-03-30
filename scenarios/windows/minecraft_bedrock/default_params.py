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
    Params.setDefault('minecraft_bedrock', 'duration', '300', desc='Duration Of Test', valOptions=[])
    Params.setParam(None, 'loop_duration', '600')
    Params.setParam(None, 'final_loop_duration', '0')
    Params.setParam(None, 'loops', '1')
    Params.setParam(None, 'loop_counter', '1')
    Params.setParam('global', 'dut_scaling_override', '1.5')
    return

def run_user_only():
    return
