# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from core.parameters import Params

def run():
    Params.setDefault('puget_prep', 'puget_license', '', desc='Puget License', valOptions=[])
    Params.setParam(None, 'i', '0')
    return
