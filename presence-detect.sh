#! /bin/bash

# presence-detect.sh
# searches for the MAC address of known devices

# do arp_scan to get connected mac addresses
connectedDevices=$(sudo arp-scan -l)

knownDevices=("d4:28:d5:37:7e:a2" "24:f0:94:d1:9a:e1")

for device in "${knownDevices[@]}"
do
    if [[ "$connectedDevices" = *"$device"* ]]; then
        echo "$device is present!"
    else
        echo "$device is NOT present!"
    fi
done
