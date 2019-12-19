# AirSaver - Smart Home Application

## Student Name: Grace Finnerty    
## Student ID: 20086644


AirSaver is a program that senses the temperature in your apartment! Cool, huh? (excuse the pun)

Well it dosnet stop there...

AirSaver also recognises registered devices on the home Wifi network. Why you might ask? Well as the name suggest its to "Save" - energy and money!

I dont know about you I tend to leave the AC on in my apartment quite often. So I created this program which can tell if the AC is on but Im not home and will turn it off for me! Just to remind me not to do it again, it will also tweet the twitter Account I have for my Smart home. 

And even better still if I need to turn the AC on before I return again I can - using the Blynk app - Winning! 

## Want to recreate my program? Here are the Tools, Technologies and Equipment youll need 

* Rasperberry Pi  - for all of the "computer stuff"
* Sense Hat with Temperature Sensor - to sense the temperature
* Wireless Network Watcher - becuase I barely know my phone's number let alone its MAC address
* Putty - to crack into the Pi 
* Python Program - presence_temp.py 
- This program detects who is home by checking if their phone is connected to the WiFi via the phones MAC address. 
It also senses the temperature in the apartment. If, after the phone is not present on the network any longer, the program assumes the owner is gone. If the temperature stays below 39 degrees then it is clear the AC has been left on. The program will then turn off the AC, and notify ThinkSpeak that this Auto Shutdown has taken place.
* JavaScript Program - index.js  - This is the amazing program that links to my the Blynk app on my phone. It allows me to read the temperature data from the sense hat and switch on the AC when before I return - cause no on likes coming back to a stuffy apartment 
