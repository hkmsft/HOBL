 REM Copyright (c) Microsoft. All rights reserved.
 REM Licensed under the MIT license. See LICENSE file in the project root for full license information.

schtasks /create /sc ONLOGON /tn StartHostPrograms /tr c:\hobl\setup\src\host_start.cmd /f
powershell.exe Set-ExecutionPolicy Unrestricted -Force