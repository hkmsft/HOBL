# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from core.parameters import Params

def run():
    Params.setDefault('web_close_tabs', 'num_tabs_to_close', '1', desc='Number of tabs to close', valOptions=[])
    return
