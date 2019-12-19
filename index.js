var Blynk = require("blynk-library");

var sense = require("node-sense-hat");
var imu = sense.Imu;
var IMU = new imu.IMU();

var AUTH = 'r8FMCRRE_aCKSjblNMc6xxJucgO0fm0Q';

var blynk = new Blynk.Blynk(AUTH);


var v2 = new blynk.VirtualPin(2);
var v3 = new blynk.VirtualPin(3);


var white = [255, 255, 255];
sense.Leds.clear();

var wia = require('wia')('d_sk_VLdArRU3IwmPa6o6eJp4yTfV');

// v1 sends temperature data to the Blynk App


v2.on('read', function() {
  IMU.getValue(function (e, data) {
     v2.write(data.temperature);
  })
});

// v3 is connected to a button on the app which when press will cause the pi to light up and will notify the pi to be switched on 
v3.on('write', function(param) {
  console.log('V3:', param[0]);
  if (param[0]==1){
        sense.Leds.clear(white)
	//this button being pressed will tell the pi to switch on the AC unit
    }else{
        sense.Leds.clear();
    }
});



wia.stream.connect();
