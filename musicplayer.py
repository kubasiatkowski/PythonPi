#Simple music player using SenseHat
# Path (volume serial of USB stick) is hardcoded
# and the code is not portable
#

from sense_hat import SenseHat
from random import randint
from pygame import mixer
import glob,os,random

#initialize sound mixer
mixer.init()

#initialize SenseHat
sense = SenseHat()
sense.clear()

#change dir if you want to reuse the code
os.chdir("/media/pi/1EB8-AEB7/muzyka")
songs = glob.glob("*.mp3")


 
#infinite loop
while True:
	#read joystick
    for event in sense.stick.get_events():
		#next song
        if event.action == 'pressed' and event.direction == 'right':
            mixer.music.load(random.choice(songs))
            mixer.music.play()
		#stop
        if event.action == 'pressed' and event.direction == 'middle':
            mixer.music.stop()
		#volume up
        if event.action == 'pressed' and event.direction == 'up':
            mixer.music.set_volume(mixer.music.get_volume()+0.1)    
		#volume down
        if event.action == 'pressed' and event.direction == 'down':
            mixer.music.set_volume(mixer.music.get_volume()-0.1)
	#get volume as int between 0,7
    volume=(int)(mixer.music.get_volume()*7)
	
	#random sparkling leds
    sense.set_pixel(randint(0,6),randint(0,7),randint(0,255),randint(0,255),randint(0,255))
    
	#show volume indicator
    for i in range (0,7):
        if i < volume:
            sense.set_pixel (7,i,(255,0,0))
        else:
            sense.set_pixel (7,i,(0,0,0))
            

