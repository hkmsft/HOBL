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
    Params.setDefault('mac_puget_ps', 'benchmark_version', '1.0.5', desc='Benchmark Version', valOptions=[])
    Params.setDefault('mac_puget_ps', 'puget_license', '', desc='Puget License Key', valOptions=[])
    Params.setDefault('mac_puget_ps', 'loops', '1', desc='Amount of Loops for Test', valOptions=[])
    return

def run_user_only():
    Params.setDefault('mac_puget_ps', 'benchmark_version', '1.0.5', desc='Benchmark Version', valOptions=[])
    Params.setDefault('mac_puget_ps', 'puget_license', '', desc='Puget License Key', valOptions=[])
    Params.setDefault('mac_puget_ps', 'loops', '1', desc='Amount of Loops for Test', valOptions=[])
    return
