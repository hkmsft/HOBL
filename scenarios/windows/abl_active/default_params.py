# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from core.parameters import Params

def run():
    Params.setParam(None, 'web_replay_run', '1')
    Params.setDefault('abl_active', 'idle_time', '111', desc='Idle time between each app switch, - 3s', valOptions=[])
    Params.setParam(None, 'phase_reporting', '1')
    return
