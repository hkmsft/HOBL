# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

param (
    [string]$version
)

$rule = "web_replay_$version"
$program  = "C:\web_replay\$version\bin\web_replay.exe"

netsh advfirewall firewall show rule name="$rule" | Out-Null

if ($LASTEXITCODE -eq 1) {
    Write-Output "$rule does not exist"
}

exit 0
