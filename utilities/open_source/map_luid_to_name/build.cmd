@echo off
:: Copyright (c) Microsoft. All rights reserved.
:: Licensed under the MIT license. See LICENSE file in the project root for full license information.

mkdir build_x64
pushd build_x64
cmake -S .. -A x64
cmake --build . --config Release
popd

mkdir build_arm64
pushd build_arm64
cmake -S .. -A arm64
cmake --build . --config Release
popd

mkdir x64
copy build_x64\Release\map_luid_to_name.exe x64

mkdir arm64
copy build_arm64\Release\map_luid_to_name.exe arm64
