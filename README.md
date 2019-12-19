# AirSaver - Smart Home Application

## Student Name: Grace Finnerty    
## Student ID: 20086644

AirSaver is a program that senses the temperature in my apartment, it also recognises the devices on the home Wifi network. 
I tend to leave the AC on in my apartment quite often, wasting energy and money. This program aims to notifiy me if I am not in the apartment but the AC is still running. 

## Tools, Technologies and Equipment

* Rasperberry Pi 
* Putty
* Wireless Network Watcher
* Sense Hat with Temperature Sensor
* Python Program - presence_temp.py 
This program detects who is home by checking if their phone is connected to the WiFi via the phones MAC address. 
It also senses the temperature in the apartment. If, after the phone is not present on the network any longer, the program assumes the owner is gone. If the temperature stays below 39 degrees then it is clear the AC has been left on. The program will then turn off the AC, and notify ThinkSpeak that this Auto Shutdown has taken place.
