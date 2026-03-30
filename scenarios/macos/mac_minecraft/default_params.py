# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from core.parameters import Params

def run():
    Params.setDefault('mac_minecraft', 'duration', '300', desc='Duration of Minecraft Game', valOptions=[])
    return
