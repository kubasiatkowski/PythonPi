#Very simple Pong for RaspberyPi and SenseHat
#(c) Kuba Siatkowski

import time
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(180)
sense.clear()
#ball
x, y = 4, 7

#pad
pl, pr = 3 , 4

#ball move
xi, yi = -1, -1

#initial speed
speed = 0.5

#speed up factor
speedinc = 0.05

#initial points
points = 0

#grow pad every x points
growth = 5

while True:
    sense.clear()
	
	#move and draw the ball
    if x == 7:
        xi = -1
    if x == 0:
        xi = 1
    x = x + xi
    y = y + yi
    sense.set_pixel(x, y, ((x * 16), (255 - x * 16), (255 - x * y)))

	#move the pad
    for event in sense.stick.get_events():
        if event.action == 'pressed' and event.direction == 'right':
            if pl > 0:
                pl -= 1
                pr -= 1
           
        if event.action == 'pressed' and event.direction == 'left':
            if pr < 7:
                pr += 1
                pl += 1
		#distraction when middle button is pressed		
        if event.action == 'pressed' and event.direction == 'middle':
            sense.clear(48,48,48)
    #draw the pad
    for i in range (0,8):
        if i < pl:
            sense.set_pixel (i,0,(0,0,0))
        elif i > pr:
            sense.set_pixel (i,0,(0,0,0))
        else:
            sense.set_pixel (i,0,(255,255,255))

    time.sleep(speed)
    if y == 7:
        yi = -1
    if y == 1:
		#if ball hit the pad
        if pl -1 <= x <= pr + 1:
            yi = 1
            points = points + 1
            speed = speed * 0.8
            #increase speed 
            if speed < 0:
                speed = 0.025
			#make the pad wider
            if points % growth == 0:
                if pl >= 1:
                    pl -= 1
                else:
                    pr += 1
		#reset the game if ball missed the pad
        else:
            sense.clear(255,0,0)
            speed = 0.5
            points  = 0
            pl, pr = 3,4
            3,4
            time.sleep(1)
            x = 4
            y = 7
	#reset pad size if it is too wide
    if pr > 8:
        sense.clear(0,255,0)
        time.sleep(0.5)
        pl, pr = 3,4
        speed = speed * 20

	#debug messages
    msg = "x = {0}, y = {1}, pr = {2}, pl = {3}, speed = {4}, points = {5}".format(x, y ,pr, pl, speed, points)
    print (msg)
            
            
            

