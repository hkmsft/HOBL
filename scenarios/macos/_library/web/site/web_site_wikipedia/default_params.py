# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from core.parameters import Params

def run():
    Params.setDefault('web_site_wikipedia', 'new_tab', '0', desc='', valOptions=['0', '1'])
    Params.setDefault('web_site_wikipedia', 'load_only', '0', desc='', valOptions=['0', '1'])
    return
