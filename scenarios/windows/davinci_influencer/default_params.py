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
    import_run_user_only('..\\_library\\davinci\\clear_render_queue')
    import_run_user_only('..\\_library\\davinci\\open_davinci')
    import_run_user_only('davinci\\add_effects')
    import_run_user_only('davinci\\add_media')
    import_run_user_only('davinci\\add_music')
    import_run_user_only('davinci\\add_vid1_first_eff')
    import_run_user_only('davinci\\delete_bench')
    import_run_user_only('davinci\\edit_clip_params')
    import_run_user_only('davinci\\edit_timeline_settings')
    import_run_user_only('davinci\\keyboard_customization')
    import_run_user_only('davinci\\open_davinci')
    import_run_user_only('davinci\\render2')
    return
