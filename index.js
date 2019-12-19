var Blynk = require("blynk-library");

var sense = require("node-sense-hat");
var imu = sense.Imu;
var IMU = new imu.IMU();

var AUTH = 'r8FMCRRE_aCKSjblNMc6xxJucgO0fm0Q';

var blynk = new Blynk.Blynk(AUTH);

var v1 = new blynk.VirtualPin(1);
var v2 = new blynk.VirtualPin(2);
var v3 = new blynk.VirtualPin(3);
var v4 = new blynk.VirtualPin(4);

var white = [255, 255, 255];
sense.Leds.clear();

var wia = require('wia')('d_sk_VLdArRU3IwmPa6o6eJp4yTfV');

// v1 write call back
v1.on('write', function(param) {
     var colour = param.map(Number);
     sense.Leds.clear(colour);
});

v2.on('read', function() {
  IMU.getValue(function (e, data) {
     v2.write(data.temperature);
  })
});
v3.on('write', function(param) {
  //has the button been pressed??
	var button = 
    console.log("It's a bit dark");
    dark=true;
    //You could do something interesting here like turn on lights!!!!
  }
  else
  {
   dark=false;
  }
});
v4.on('write', function(param) {
 console.log("v4: lat. " + param[0])
 wia.locations.publish({
  latitude: param[0],
  longitude: param[1]
});
});

wia.stream.connect();
