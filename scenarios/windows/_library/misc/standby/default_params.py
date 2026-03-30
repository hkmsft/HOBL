# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from core.parameters import Params

def run():
    Params.setDefault('standby', 'standby_duration', '2348', desc='Time to be in standby, in seconds', valOptions=[])
    Params.setDefault('standby', 'sleep_mode', 'Standby', desc='Sleep mode', valOptions=['Standby', 'S1', 'S3'])
    return
