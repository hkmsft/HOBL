# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from core.parameters import Params

def run():
    Params.setDefault('puget_ae', 'benchmark_version', '1.1.0', desc='Benchmark Version', valOptions=[])
    Params.setDefault('puget_ae', 'puget_license', '', desc='Puget License Key', valOptions=[])
    Params.setDefault('puget_ae', 'loops', '1', desc='Amount of Loops for Test', valOptions=[])
    return
