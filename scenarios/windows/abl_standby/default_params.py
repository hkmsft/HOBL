# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from core.parameters import Params

def run():
    Params.setDefault('abl_standby', 'standby_duration', '2348', desc='The time to be in standby, in seconds', valOptions=[])
    Params.setDefault('abl_standby', 'sleep_mode', 'Standby', desc='', valOptions=['Standby', 'S1', 'S3'])
    Params.setParam(None, 'web_replay_run', '1')
    return
