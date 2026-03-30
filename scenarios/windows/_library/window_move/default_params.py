# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from core.parameters import Params

def run():
    Params.setDefault('window_move', 'screen', '0', desc='Display to use', valOptions=[])
    return
