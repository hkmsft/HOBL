# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from core.parameters import Params

def run():
    Params.setDefault('test_param', 'test1', '0', desc='', valOptions=[])
    Params.setDefault('web', 'test2', '1', desc='', valOptions=[])
    Params.setParam(None, 'test3', '0')
    Params.setParam('idle_desktop', 'duration', '5')
    return
