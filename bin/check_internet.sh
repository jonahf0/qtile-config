#!/bin/bash

line=$(nmcli -f name,device -t -m tabular connection | rg wlp2s0)

printf "$(echo -n $line | cut -d ":" -f 2): '$(echo -n $line | cut -d ":" -f 1)'"