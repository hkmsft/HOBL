# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

# Build SimpleTimer for macOS
# Must be run on a macOS machine with Xcode Command Line Tools installed

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BIN_DIR="${SCRIPT_DIR}/bin"

mkdir -p "${BIN_DIR}"

echo "Building SimpleTimer..."
clang++ -std=c++11 -Wall -Wextra -O2 -o "${BIN_DIR}/SimpleTimer" "${SCRIPT_DIR}/timers.cpp"

echo "Build complete: ${BIN_DIR}/SimpleTimer"
