# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

##
# invoke cs_groove scenario with paused param set 
##
import builtins
from core.parameters import Params
Params.setOverride('cs_groove', 'paused', '1')
import scenarios.windows.cs_groove
Params.setAssociatedSections('cs_groove_paused', ['cs_groove'])

class CsGroovePaused(scenarios.windows.cs_groove.CsGroove):
    pass

   