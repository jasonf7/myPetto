## Authors: Jason Fang, Zuqi Li, Jesse Jie, Andrew Zhou, Eric Pei
## Jake Si
## Date: November 27, 2013
## Subject: SE101
## Description: This file contains functions that handle the food and fetch sub-processes.

from myro import *
import random

## Name: openFoodFile()
## Parameters: None
## Description: Generates lists of the food names and their RGB values 
## from the "food.txt" file.
## Do not run this function explicitly
## Helper function for hungry()
def openFoodFile():
	f=open("food.txt","r")
	foods=[]
	food_name=[]
	
	for line in f:
		foods.append(line.split())
		
	food_code=[[] for x in xrange(len(foods))]
	
	for i in range(0, len(foods)):
		food_name.append(foods[i][0])
		for j in range(1,len(foods[i])):
			food_code[i].append(int(foods[i][j]))		

	f.close()
	
	return [food_code, food_name]

## Name: hungry()
## Parameters: foodName - A string of the food that the pet wants to eat
## Description: Handles the food eating subprocess.
## Controls behaviour and interaction of the pet when it is hungry.
## Returns 1 on successful completion of function
def hungry(foodName):
##        print foodName
	VARIANCE = 25
	food_code, food_name = openFoodFile()
	iWantToEatThis = foodName
	n = food_name.index(foodName)
	hungrySound = makeSong("G .5; E .5;")
	successSound = makeSong("REST 2; D 1; D .25; D .5; A 1")
	
	while(True):
                setLED("left", "off")
                setLED("right", "off")
                setLED("front", "off")
                setLED("back", "off")
                autoCamera()
		robot.playSong(hungrySound)
		img = takePicture()
		r = g = b = 0
		
		for i in range(getWidth(img)/4, getWidth(img)*3/4):
			for j in range(getHeight(img)/4,getHeight(img)*3/4):
				pixel = getPixel(img,i,j)
				r_tmp, g_tmp, b_tmp = getRGB(pixel)
				r += r_tmp
				g += g_tmp
				b += b_tmp
				
		r /= getWidth(img)/2 * getHeight(img)/2
		g /= getWidth(img)/2 * getHeight(img)/2
		b /= getWidth(img)/2 * getHeight(img)/2
##		print (r, g, b)
		
		if ((food_code[n][0] in xrange(r-VARIANCE, r+VARIANCE)) and (food_code[n][1] in xrange(g-VARIANCE, g+VARIANCE)) and (food_code[n][2] in xrange(b-VARIANCE, b+VARIANCE))):
			robot.playSong(successSound)
##			show(img)
			return 1

## Name: fetch()
## Parameters: None
## Description: Handles the fetch subprocess.
## Controls behaviour and interaction of the pet when it is playing fetch.
## Returns 1 on successful completion of function
def fetch():
	VARIANCE = 25
	fetchSound = makeSong("E .5; E .25; E .5; C .25; E .5; G .5;")
	successSound = makeSong("REST 2; D 1; D .25; D .5; A 1")
	fetchColor = [38, 27, 46]
	n = 0
	
	while(True):
##                autoCamera()
		robot.playSong(fetchSound)
		img = takePicture()
		r = g = b = 0
		
		for i in range(getWidth(img)/4, getWidth(img)*3/4):
			for j in range(getHeight(img)/4,getHeight(img)*3/4):
				pixel = getPixel(img,i,j)
				r_tmp, g_tmp, b_tmp = getRGB(pixel)
				r += r_tmp
				g += g_tmp
				b += b_tmp
				
		r /= getWidth(img)/2 * getHeight(img)/2
		g /= getWidth(img)/2 * getHeight(img)/2
		b /= getWidth(img)/2 * getHeight(img)/2
		
		if ((fetchColor[0] in xrange(r-VARIANCE, r+VARIANCE)) and (fetchColor[1] in xrange(g-VARIANCE, g+VARIANCE)) and (fetchColor[2] in xrange(b-VARIANCE, b+VARIANCE))):
			print "Good job!"
			forward(1, 1)
			n += 1
			if n >= 5:
				robot.playSong(successSound)
				stop()
				return 1

# hungry()			
