# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from core.parameters import Params

def run():
    Params.setDefault('param_test_compnents', 'my_param', '0', desc='', valOptions=['0', '1'])
    return
