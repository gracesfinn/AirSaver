#!/usr/bin/env python coding=utf-8

import subprocess
import logging
import urllib2
import  json
import  time

logging.basicConfig(filename='/home/pi/AirSaver/presence-detector.log',level=logging.INFO, format='%(asctime)s - %(message)s')
logging.info('Starting presence detector')

from sense_hat import SenseHat
from time import sleep

WRITE_API_KEY='F5GSNHD01VIEIAU3'

baseURL='https://api.thingspeak.com/update?api_key=%s' % WRITE_API_KEY


#Names of device owners
names = ["Grace"]

#MAC address of device
macs = ["24:f0:94:d1:9a:e1"]

#Temperature from SenseHat
from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

#Defining colour for the text on the LED screen
blue = (0,128,128)


#Code which combines presence detection and temperature sensors 
#Has the AC been left on?
def arp_scan():
        try:
                output = subprocess.check_output("sudo arp-scan -l", shell=True)
                for i in range(len(names)):
                        result = names[i]
			temp = sense.get_temperature()
                        if (macs[i] in output and temp <=39):
                                result=result+" is home and AC is on"
				tsFlag = 0 #ThingSpeak Flag for 0
                        else:
                                result=result+" is not home - Auto AC shutdown"
				tsFlag = 1 #ThingSpeak Flag which will send a tweet to ThingSpeak and then to the sudo HTTP "AC Unit"
                        print(result)
                        sense.show_message(result, text_colour = blue)
			return tsFlag
        except Exception as e:
                logging.error(e)


#ThingSpeak Code
def writeData(tsFlag):
    # Sending the data to thingspeak in the query string
    conn = urllib2.urlopen(baseURL + '&field1=%s' % (tsFlag))
    print(conn.read())
    # Closing the connection
    conn.close()


while True:
	tsFlag=arp_scan()
	writeData(tsFlag)
        time.sleep(30)




