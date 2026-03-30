# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from core.parameters import Params

def run():
    Params.setDefault('global', '[idle_time]', '111', desc='Idle time between each app switch, - 3s', valOptions=[])
    return
