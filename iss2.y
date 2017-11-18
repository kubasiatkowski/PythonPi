from sense_hat import SenseHat
from time import sleep 
from random import randint
sense = SenseHat()
sense.set_rotation(270)

l=(78, 101, 237) #light blue
d=(3, 12, 68) #dark blue
g=(3, 154, 68) #green
y=(255, 255, 149) #yellow
r=(255,0,0) #red
p=(153, 51, 255) #purple

# Generate a random colour
def t():
  random_red = randint(0, 255)
  random_green = randint(0, 255)
  random_blue = randint(0, 255)
  return (random_red, random_green, random_blue)


sense.show_message("Hey ISS",scroll_speed=0.05,text_colour=p)
sense.show_message("greetings from Earth",scroll_speed=0.05,text_colour=y)
sense.show_message("KALINA",scroll_speed=0.05,text_colour=l)



temperature=round(sense.get_temperature(), 1 )

sense.show_message("Temperature: " + str(temperature),back_colour=d,text_colour=(255,128,128), scroll_speed=0.05)
while True:
  heart = [
    d,d,d,d,d,d,d,d,
    d,r  ,r  ,d  ,d  ,r  ,r  ,d,
    r,t(),t(),r,r,t(),t(),r,
    r,t(),t(),t(),t(),t(),t(),r,
    d,r,t(),t(),t(),t(),r,d,
    d,d,r,t(),t(),r,d,d,
    d,d,d,r,r,d,d,d,
    d,d,d,d,d,d,d,d
    ]
  sense.set_pixels(heart)
 
