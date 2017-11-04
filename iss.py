from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.set_rotation(270)

l=(78, 101, 237) #light blue
d=(3, 12, 68) #dark blue
g=(3, 154, 68) #green
y=(255, 255, 149) #yellow
r=(255,0,0) #red
p=(153, 51, 255) #purple

earth1 = [
    d,d,d,y,d,d,d,y,
    d,d,l,l,l,g,d,d,
    y,l,g,l,g,g,l,d,
    d,g,g,l,g,g,g,d,
    d,l,g,l,l,l,l,y,
    d,l,l,l,g,l,l,d,
    d,d,g,l,g,g,d,d,
    d,y,d,d,d,y,d,d
]

earth2 = [
  d,d,y,d,d,d,y,d,
  d,d,l,l,l,l,d,d,
  d,l,l,g,l,g,g,d,
  y,l,g,g,l,g,g,d,
  d,l,l,g,l,l,l,y,
  d,l,l,l,l,g,l,d,
  d,d,l,g,l,g,d,d,
  d,y,d,d,y,d,d,y
]

earth3 = [
  d,d,d,y,d,d,d,y,
  y,d,l,l,l,l,d,d,
  d,l,l,l,g,l,g,d,
  d,l,l,g,g,l,g,d,
  d,g,l,l,g,l,l,d,
  y,l,l,l,l,l,g,y,
  d,d,l,l,g,l,d,d,
  y,d,y,d,d,y,d,d
  ]
  
heart1 = [
  d,d,d,d,d,d,d,d,
  d,d,d,d,d,d,d,d,
  d,d,d,d,d,d,d,d,
  d,d,d,r,d,d,d,d,
  d,d,d,d,d,d,d,d,
  d,d,d,d,d,d,d,d,
  d,d,d,d,d,d,d,d,
  d,d,d,d,d,d,d,d
  ]  
  
heart2 = [
  d,d,d,d,d,d,d,d,
  d,d,d,d,d,d,d,d,
  d,d,d,d,d,d,d,d,
  d,d,d,r,r,d,d,d,
  d,d,d,r,r,d,d,d,
  d,d,d,d,d,d,d,d,
  d,d,d,d,d,d,d,d,
  d,d,d,d,d,d,d,d
  ]  

heart3 = [
  d,d,d,d,d,d,d,d,
  d,d,d,d,d,d,d,d,
  d,d,r,d,d,r,d,d,
  d,d,r,r,r,r,d,d,
  d,d,r,r,r,r,d,d,
  d,d,d,r,r,d,d,d,
  d,d,d,d,d,d,d,d,
  d,d,d,d,d,d,d,d
  ]  

heart4 = [
  d,d,d,d,d,d,d,d,
  d,d,d,d,d,d,d,d,
  d,r,r,d,d,r,r,d,
  d,r,r,r,r,r,r,d,
  d,r,r,r,r,r,r,d,
  d,d,r,r,r,r,d,d,
  d,d,d,r,r,d,d,d,
  d,d,d,d,d,d,d,d
  ]  

heart5 = [
  d,d,d,d,d,d,d,d,
  d,r,r,d,d,r,r,d,
  r,r,r,r,r,r,r,r,
  r,r,r,r,r,r,r,r,
  d,r,r,r,r,r,r,d,
  d,d,r,r,r,r,d,d,
  d,d,d,r,r,d,d,d,
  d,d,d,d,d,d,d,d
  ]  

heart6 = [
  d,d,d,d,d,d,d,d,
  d,r,r,d,d,r,r,d,
  r,l,l,r,r,l,g,r,
  r,l,l,g,g,l,g,r,
  d,r,l,l,l,l,r,d,
  d,d,r,l,g,r,d,d,
  d,d,d,r,r,d,d,d,
  d,d,d,d,d,d,d,d
  ] 
  
sense.show_message("Hey ISS",scroll_speed=0.05,text_colour=p)
sense.show_message("greetings from Earth",scroll_speed=0.05,text_colour=y)
sense.show_message("KALINA",scroll_speed=0.05,text_colour=l)

#show earth
sense.set_pixels(earth1)
sleep(0.5)
sense.set_pixels(earth2)
sleep(0.5)
sense.set_pixels(earth3)
sleep(1)

#show hearth
sense.set_pixels(heart1)
sleep(0.2)
sense.set_pixels(heart2)
sleep(0.2)
sense.set_pixels(heart3)
sleep(0.2)
sense.set_pixels(heart4)
sleep(0.2)
sense.set_pixels(heart5)
sleep(0.2)
sense.set_pixels(heart6)
sleep(0.5)
sense.clear(d)
sense.set_pixels(heart6)
sleep(0.5)
#show earth
sense.set_pixels(earth1)
sleep(0.5)
sense.set_pixels(earth2)
sleep(0.5)
sense.set_pixels(earth3)
sleep(0.5)
sense.set_pixels(heart6)
sleep(0.5)
#show earth
sense.set_pixels(earth1)
sleep(0.5)
sense.set_pixels(earth2)
sleep(0.5)
sense.set_pixels(earth3)
sleep(0.5)
sense.set_pixels(heart6)
sleep(0.5)
sense.clear(d)

temperature=round( sense.get_temperature(), 1 )

sense.show_message("Temperature: " + str(temperature),back_colour=d,text_colour=(255,128,128), scroll_speed=0.05)
sense.set_pixels(heart6)
sleep(2)
