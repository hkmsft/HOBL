# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from functools import partial
import os
from parameters import Params
import utilities.modules

import_run_user_only = partial(utilities.modules.import_run_user_only, here=__file__)

def run():
    Params.setCalculated('scenario_section', __package__.split('.')[-1])
    run_user_only()
    return

def run_user_only():
    import_run_user_only('..\\prod_excel_close')
    import_run_user_only('..\\prod_excel_switchto')
    import_run_user_only('..\\prod_powerpoint_close')
    import_run_user_only('..\\prod_powerpoint_switchto')
    import_run_user_only('..\\prod_word_close')
    import_run_user_only('..\\prod_word_switchto')
    return
