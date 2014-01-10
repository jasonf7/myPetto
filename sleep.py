## Authors: Jason Fang, Zuqi Li, Jesse Jie, Andrew Zhou, Eric Pei
## Jake Si
## Date: November 27, 2013
## Subject: SE101
## Description: This script handles the event where the user wants the pet
## to sleep

from myro import *
import random
import time
import os

## Name: needToSleep()
## Parameters: None       
## Description: This is the main function for handling how the pet
## sleeps. It requires no helper functions at all, and is the function
## the master script (main.py) calls when it wants the pet to go to 
## sleep
def needToSleep():
	start=time.clock()
	while (time.clock()-start)<20: # define 20 seconds to be how long the user has to put the pet to sleep
		os.system('cls')
		if getBright("center") < 1000000: #define 1000000 to be threshold for when the pet is "in a dark environment"
			print "Sleeping..."
			time.sleep(5)
			print "Sleep Complete!"
			break
		else:
			print "Time Left: "+str(20-(round(time.clock()-start,2)))
	
	if (time.clock()-start)<20: # check if pet really did sleep or not
		beep(0.5, 800)
		beep(0.5, 700)
		beep(0.5, 600)
		beep(0.5, 500)
		beep(0.5, 400)
		return True
	else:
		return False
