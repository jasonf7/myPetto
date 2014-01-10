## Authors: Jason Fang, Zuqi Li, Jesse Jie, Andrew Zhou, Eric Pei
## Jake Si
## Date: November 27, 2013
## Subject: SE101
## Description: This script handles all the parts of the event where the
## pet needs to go to the washroom

from myro import *
import random
import time
import os

## Name: checkTrack()
## Parameters: None       
## Description: Helper function for NeedToPoop() that checks 
## whether both sensors are on the track or not. Return True 
## if it is, False otherwise
def checkTrack():
	if getLine("left") and getLine("right"):
		return True;
	else:
		return False;

## Name: trackMove()
## Parameters: None       
## Description: This helper function makes the robot progress
## through the track backwards since the sensors lead the robot
## this way. If one sensor is off the track then the robot
## adjusts accordingly to get both sensors on the track before
## moving again.
def trackMove():
	move(-.1,0)
	if getTurnDir()=="left":
		stop()
		rotate(.1)
		while True:
			if getTurnDir()==0:
				stop()
				break
	
	if getTurnDir()=="right":
		stop()
		rotate(-.1)
		while True:
			if getTurnDir()==0:
				stop()
				break

## Name: getTurnDir()
## Parameters: None       
## Description: This helper function returns which direction
## the robot should be turning to adjust such that
## both sensors are on the track again. It returns the
## correct direction if one of the sensors are off,
## 0 otherwise
def getTurnDir():
	if getLine("left") and not getLine("right"):
		return "left"
	elif not getLine("left") and getLine("right"):
		return "right"
	else:
		return 0

## Name: needToPoop()
## Parameters: None       
## Description: This is the main function called that uses all the helper
## function to make the robot go to the washroom and back.
def needToPoop():
	start=time.clock()
	didStart=False
	while (time.clock()-start)<20: # define 20seconds to be how long the user has to help the pet
		os.system('cls')
		if not checkTrack(): #check if the robot has been placed on the track
			print "Time Left: "+str(30-(round(time.clock()-start,2)))+"s"
		else:
			print "Going to the washroom..."
			didStart=True
			startMovement()
			print "All done!"
			time.sleep(2)
			return True
			break

	return didStart

## Name: startMovement()
## Parameters: None       
## Description: This function handles the events the pet encounters
## while going to the washroom	
def startMovement():
	while getLine("right") or getLine("left"): # moves to the washroom
		trackMove()
		
	stop()
	beep(2, 700) # poops
	rotate(-.1) # rotates to head the opposite direction back
	while True:
		if getLine("right") and getLine("left"):
			stop()
			break
	
	while getLine("right") or getLine("left"):
		trackMove()
	
	stop()
