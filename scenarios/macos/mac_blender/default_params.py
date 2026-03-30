# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from core.parameters import Params

def run():
    Params.setDefault('mac_blender', 'benchmark_option', 'CPU', desc='Selecting which device to benchmark', valOptions=['CPU', 'METAL'])
    return
