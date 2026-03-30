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
    import_run_user_only('..\\..\\run_command')
    Params.setUserDefault('teams', 'parse_MSTeams_Logs', '1', desc='Set to 1 to parse Teams logs after collecting them.', valOptions=['0', '1'])
    Params.setUserDefault('teams', 'parser_location', '..\\ScenarioAssets\\Teamsdecode\\bin\\UnifiedLogging', desc='Sets the path to the parser to use to decode Teams logs.', valOptions=[])
    return
