# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from core.parameters import Params

def run():
    Params.setDefault('mac_web', 'loops', '1', desc='', valOptions=[])
    Params.setParam(None, 'web_replay_run', '1')
    Params.setParam(None, 'phase_reporting', '1')
    return
