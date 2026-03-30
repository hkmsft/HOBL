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
    Params.setDefault('cyberpunk', 'benchmark_loops', '3', desc='Amount of Loops for Benchmarking', valOptions=[])
    Params.setDefault('cyberpunk', 'game_location', 'C:\GOG Games\Cyberpunk 2077', desc='Location of Cyberpunk Game', valOptions=[])
    return

def run_user_only():
    return
