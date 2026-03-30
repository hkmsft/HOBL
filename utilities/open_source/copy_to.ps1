# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

param(
	[string]$Address = '127.0.0.1',
	[string]$source = "",
	[string]$dest = ""
)

#Push-Location -Path (Split-Path $MyInvocation.MyCommand.Path -Parent)
open-device $address

cmdd mkdir $dest
putd $source $dest

Close-Device
#Pop-Location
