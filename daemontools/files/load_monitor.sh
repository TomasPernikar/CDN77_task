#!/bin/bash

output_file="/var/log/load_monitor.log"

while true; do
    # aktualni load
    load=$(cat /proc/loadavg | awk '{ print $1 }')

    timestamp=$(date +"%Y-%m-%d %H:%M:%S")

    # output file
    echo "$timestamp - Load: $load" >> "$output_file"

    # monitoring a 5 min
    sleep 300
done

