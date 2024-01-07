#!/bin/bash

# Get the uptime in seconds
uptime_seconds=$(awk -F. '{print $1}' /proc/uptime)

# Check if the uptime is longer than 1 minute
if [[ $uptime_seconds -gt 60 ]]; then
    echo "Uptime is longer than 1 minute"
else
    echo "Uptime is less than 1 minute"
    echo $uptime_seconds
    
    
    bash Desktop/pairbluetooth.sh
    
    amixer sset Master 100%
    pico2wave -w=test.wav "Welcome to to see, A smart glasses for better vision."
    aplay test.wav
    
    # Enable wifi
    iwconfig
    ifconfig
    sudo dhclient wlan0
    
    # Starting main code
    source Desktop/FR/tfenv2/bin/activate
    cd Desktop/ML
    python3 pi_driver.py
fi


