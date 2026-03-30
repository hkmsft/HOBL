# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from functools import partial
import os
from parameters import Params
from utilities.modules import import_run_user_only

def run():
    Params.setCalculated('scenario_section', __package__.split('.')[-1])
    run_user_only()
    return

def run_user_only():
    import_run_user_only('scenarios\\MacOS\\_library\\productivity\\prod_excel_open')
    import_run_user_only('scenarios\\MacOS\\_library\\productivity\\prod_onenote_open')
    import_run_user_only('scenarios\\MacOS\\_library\\productivity\\prod_outlook_open')
    import_run_user_only('scenarios\\MacOS\\_library\\productivity\\prod_powerpoint_open')
    import_run_user_only('scenarios\\MacOS\\_library\\productivity\\prod_word_open')
    return
