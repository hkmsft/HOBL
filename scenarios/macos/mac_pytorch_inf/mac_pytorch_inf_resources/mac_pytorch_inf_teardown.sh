#!/bin/sh
# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

# Set BIN_DIR to /Users/Shared/hobl_bin
BIN_DIR="/Users/Shared/hobl_bin"
LOG_DIR="/Users/Shared/hobl_data"
LOG_FILE="$LOG_DIR/mac_pytorch_inf_teardown.log"
mkdir -p "$LOG_DIR"

log() {
    echo "$1"
    echo "$1" >> "$LOG_FILE"
}

# Create assets folder if it does not exist
if [ ! -d $BIN_DIR ]; then
    mkdir $BIN_DIR
fi

echo "-- mac_pytorch_inf_teardown.sh started $(date)" > "$LOG_FILE"
log "-- pytorch_inf teardown started"

# Source profile to load brew + pyenv
log "-- Loading environment"
if [ -f ~/.zprofile ]; then
    source ~/.zprofile
else
    log " ERROR - ~/.zprofile not found"
    exit 1
fi

log "-- Setting Python version"
pyenv global 3.12.10

log "-- CD to resources"
cd $BIN_DIR/mac_pytorch_inf_resources

log "-- Cleanup GPU caching"
python inference.py --cleanup-gpu

log "-- pytorch_inf teardown completed"
exit 0