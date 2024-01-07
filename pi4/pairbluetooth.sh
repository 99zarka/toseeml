#!/bin/bash

mac_address= "F7:72:10:FA:05:ED"

# Check if the speaker is already connected
if bluetoothctl info "$mac_address" | grep -q 'Connected: yes'; then
    echo "Speaker is already connected"
else
    # Connect to the speaker
    echo "pairing to speaker..."
    bluetoothctl pair "F7:72:10:FA:05:ED"
    
    amixer sset Master 100%
    pico2wave -w=test.wav "Pairing with blutooth speaker."
    aplay test.wav
    
    for i in {0..60}; do
        # Check the pairing status of the device
        pairing_status=$(bluetoothctl info "F7:72:10:FA:05:ED" | grep "Paired")
        echo "Attemting to pair"
        echo $pairing_status

        # If the device is paired, exit the loop
        if [[ $pairing_status =~ "Paired" ]]; then
            break
        fi

        # Sleep for 1 second
        sleep 1
    done
    bluetoothctl connect "F7:72:10:FA:05:ED"
    pactl set-default-sink "bluez_sink.F7_72_10_FA_05_ED.a2dp_sink"
    sleep 5
fi
    
bluetoothctl connect "F7:72:10:FA:05:ED"
pactl set-default-sink "bluez_sink.F7_72_10_FA_05_ED.a2dp_sink"
amixer sset Master 100%
pico2wave -w=test.wav "Verify if the Bluetooth speaker is working."
aplay test.wav