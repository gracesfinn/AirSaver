import urllib2
import json
import time
from sense_hat import sense_hat

WRITE_API_KEY="F5GSNHD01VIEIAU3"

baseURL='https://api.thingspeak.com/update?api_key=%s' % WRITE_API_KEY

sense = SenseHat()

def writeData(temp):
    # Sending the data to thingspeak in the query string
    conn = urllib2.urlopen(baseURL + '&field1=%s' % (temp))
    print(conn.read())
    # Closing the connection
    conn.close()

while True:
    temp=round(sense.get_temperature(),2)
    writeData(temp)
    time.sleep(60)