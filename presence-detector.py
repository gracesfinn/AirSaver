#!/usr/bin/env python
#coding=utf-8

import subprocess

import logging

logging.basicConfig(filename='/home/pi/AirSaver/presence-detector.log',level=logging.INFO, format='%(asctime)s - %(message)s')
logging.info('Starting presence detector')

from sense_hat import SenseHat

from time import sleep

sense = SenseHat()

#Names of device owners
names = ["Grace","Will"]

#MAC address of device
macs = ["24:f0:94:d1:9a:e1","74:b4:87:b2:c9:46"]

def arp_scan():
        try:
                output = subprocess.check_output("sudo arp-scan -l", shell=True)
                for i in range(len(names)):
                        result = names[i]
                        if macs[i] in output:
                                result=result+" is home"
                        else:
                                result=result+" is not home"
                        print(result)
                        sense.show_message(result)
        except Exception as e:
                logging.error(e)
while True:
	arp_scan()
	sleep(30)
