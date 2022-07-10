#!/bin/bash

TERMS=("alacritty" "st")
SHELLS=("bash" "fish" "pwsh")

R_TERM=$(shuf -i 0-1 -n 1)
R_SHELL=$(shuf -i 0-2 -n 1)

TERM=${TERMS[$R_TERM]}
SHELL=${SHELLS[$R_SHELL]}

eval "$TERM -e $SHELL"