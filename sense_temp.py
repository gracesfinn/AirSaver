from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
green = (0, 255, 0)
red = (0,0,255)
while True:
  temp = sense.get_temperature()
  if temp >=25:
    sense.show_message("AC OFF!", text_colour = red)
  else:
    sense.show_message("AC ON!", text_colour = blue)
  print(temp)
