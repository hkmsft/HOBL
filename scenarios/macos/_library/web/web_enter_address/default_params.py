# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from core.parameters import Params

def run():
    Params.setDefault('web_enter_address', 'web_site_address', 'about:blank', desc='', valOptions=[])
    Params.setDefault('web_enter_address', 'new_tab', '0', desc='', valOptions=['0', '1'])
    Params.setDefault('web_enter_address', 'web_site_load_time', '20', desc='', valOptions=[])
    return
