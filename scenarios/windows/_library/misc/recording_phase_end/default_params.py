# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from core.parameters import Params

def run():
    Params.setDefault('global', '[phase_category]', 'invalid', desc='', valOptions=[])
    Params.setDefault('global', '[phase_name]', 'invalid', desc='', valOptions=[])
    return
