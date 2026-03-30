# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

param (
    [string]$version
)

$rule = "web_replay_$version"
$program  = "C:\web_replay\$version\bin\web_replay.exe"

$addArgs = "advfirewall firewall add rule name=`"$rule`" program=`"$program`""
$addArgs += " dir=in action=allow enable=yes localport=any protocol=TCP profile=public,private,domain"

Start-Process -FilePath "netsh" -ArgumentList "$addArgs" -Verb RunAs

exit 0
