## Authors: Jason Fang, Zuqi Li, Jesse Jie, Andrew Zhou, Eric Pei
## Jake Si
## Date: November 27, 2013
## Subject: SE101
## Description: This is the main script first executed to start the program. It acts as a 
## master/control script that manages the pet's characteristics and decides
## when to make the pet do something based on user input.

#import libraries used
from myro import *
import time
import random
import math
import os
import string

# import functions used from other files
from poop import *
from sleep import *
from read import *

random.seed() # starts random generator

# starts robot and configures camera for clear pictures
init("COM4")
setLED("left", "off")
setLED("right", "off")
setLED("front", "off")
setLED("back", "off")
autoCamera()

clear = lambda: os.system('cls') #assigns clear console command to function clear

#constants
EAT=0
POOP=1
SLEEP=2
FETCH=3
fApple=0
fBlueberry=1
fGrape=2

# global variables used and constants
x=0 
HAPPY=50
percent=[50,50,50,50] # levels for all activities
food=[30,30,30] # chance the pet wants each type of food
didIdle=False

# gets random pet names from file
f = open("pName.txt") 
pName = f.readlines()
f.close()

# strips \n character from each name
for i, s in enumerate(pName):
	pName[i]=s.strip()

## Name: idle()
## Parameters: None       
## Description: This function makes the robot execute a random movement
## since it is idling.						   
def idle():
	global didIdle
	
	# generates random movement characteristics like if it
	# moves, angle, speed, time etc.
	start = time.clock()
	willMove=random.randint(0,3)
	rotate=random.uniform(-1,1)
	speed=random.uniform(-1,1)
	duration=random.uniform(1,3)
	
	if willMove==0:
		didIdle=True
		while (time.clock()-start)<duration:
			move(speed,rotate)
	else:
		time.sleep(0.5)
		didIdle=False
	stop()

## Name: changeFood()
## Parameters: None       
## Description: This function changes the chances for the pet to
## want to eat each of the three types of food by incrementing a 
## counter x. The sine waves are chosen to give an impression
## that the pet's food preference fluctuates with time.
def changeFood():
	global food
	food[fApple]=2*math.cos((2*math.pi/9)*x)+2
	food[fBlueberry]=2*math.cos((2*math.pi/9)*(x-3))+2
	food[fGrape]=2*math.cos((2*math.pi/9)*(x-6))+2

## Name: changeUI()
## Parameters: None       
## Description: This function refreshes and updates the look
## of the user interface (console).
def changeUI():
	clear()
	print string.center("myPetto User Interface: "+name, 30)
	
	# the following prints bars representing the levels of the
	# pet's need to eat, poop, sleep etc. Each character in each
	# bar should represent 4
	print "Fullness:     " + str(percent[EAT])+"% [",
	for i in range(25):
		if i <= int(percent[EAT])/4:
			print "F",
		else:
			print "-",
	print "]\n"
	
	print "POOP:         " + str(percent[POOP])+"% [",
	for i in range(25):
		if i < int(percent[POOP])/4:
			print "P",
		else:
			print "-",
	print "]\n"
	
	print "Energy Level: " + str(percent[SLEEP])+"% [",
	for i in range(25):
		if i < int(percent[SLEEP])/4:
			print "Z",
		else:
			print "-",
	print "]\n"
	
	print "Love:         " + str(percent[FETCH])+"% [",
	for i in range(25):
		if i < int(percent[FETCH])/4:
			print "F",
		else:
			print "-",
	print "]\n"
	
	print "Happiness:    " + str(HAPPY)+"% [",
	for i in range(25):
		if i < HAPPY/4:
			print "H",
		else:
			print "-",
	print "]\n"

## Name: loadBar()
## Parameters: None       
## Description: Produces an animation in the console similar
## to a loading bar to show progression of setting up the pet
## robot. This is only done for aesthetics and not actually used
## to hide any background processes happening.	
def loadBar():
	for i in range(0,101):
		speedType=random.randint(0,40) # random number to choose between high/low speed
		Lspeed=random.uniform(0.4,0.6)
		Hspeed=random.uniform(0.001,0.15)
		print "Status:",
		if i<25: # different status messages based on load progress
			print "Booting Up the Robot..."
		elif i<50:
			print "Configuring Settings..."
		elif i<75:
			print "Initializing Robot..."
		else:
			print "Finalizing Process..."

		print "Loading:",
		for j in range(0,i/4): # produces load characters
			print "@",
		for k in range(i/4,25):
			print " ",
		print str(i)+"%",
		if i>97:
			time.sleep(0.5) # load slow at the end
		elif speedType==0:
			time.sleep(Lspeed) 
		else:
			time.sleep(Hspeed)
		print "\n"
		if i!=100:
			os.system('cls')

## Name: save()
## Parameters: None       
## Description: This function takes a 'snapshot' or the pet's
## current progress and saves/writes its properties to a .save
## file to be loaded up again at any time.
def save():
	f=open(name+ '.save', 'w')
	f.write(name+ '\n')
	f.write(str(x)+ '\n')
	for i in range (0,4):
		f.write(str(percent[i])+ '\n')
	f.close()

# This marks the beginning of the real program, starting with asking the user about
# the pet he/she wants to create
choice=raw_input("Create a new pet or load a previous one? ('n' - new, 'l' - load): ")
while choice != 'n' and choice != 'l':
	choice=raw_input("Please enter a valid input-> 'n' - new, 'l' - load: ")

clear()

if choice == 'n': # new pet
	choice=raw_input("Do you want a custom or random pet name? ('c' - custom, 'r' - random): ")
	while choice != 'c' and choice != 'r':
		choice=raw_input("Please enter a valid input-> 'c'-custom or 'r'-random: ")

	if choice == 'r':
		num=random.randint(0,len(pName)-1)
		name=pName[num]
	elif choice == 'c':
		name=raw_input("Please give your pet a name: ")
elif choice == 'l':	 # load pet
	name=raw_input("Enter the name of the pet you want to load. (Case-sensitive): ")
	while not os.path.exists(name+'.save'):
		name=raw_input('Pet not found, please try again: ')
	f = open(name+'.save')
	name=f.readline().strip()
	x=int(f.readline().strip())
	for i in range (0,4):
		percent[i]=int(f.readline().strip())
	f.close()

clear()
print "Get ready to meet your new pet - " + name + "!"
time.sleep(0.5)
clear()
loadBar()

# This loops makes the bulk of the program, making the pet idle
# until the user wants to make it do something by putting him/herself
# in front of the pet.
while True:
	changeUI() #update UI
	
	# checks if the pet died, which is when one of the pet's levels hit 0.
	didDie=False
	for p in percent: 
		if p==0:
			didDie=True
	if didDie:
		clear()
		print "Oh No! "+name+" has died!"
		time.sleep(5)
		break
	
	idle()
	if getObstacle("center") > 1000: # check if the user wants it to do something
		print "What do you want to do with your pet?"
		print "Type 'e' to feed it"
		print "     'p' to take it to the bathroom"
		print "     'z' to put it to sleep"
		print "     'f' to play fetch"
		print "     'b' to go back"
		print "     's' to save your pet's state"
		print "     'x' to exit the game"
		
		event=raw_input()
		while event != 'e' and event != 'p' and event != 'z' and event != 'f' and event != 'b'  and event != 's' and event != 'x':
			print "Invalid Input: Please try again \r"
			event=raw_input()
		
		clear()
		if event == 'e': # eat event
			changeFood() # update pet food preferences
			
			maxIndex=food.index(max(food)) # Finds the food preference of the pet
			foodPref=""					   # NOTE: This does NOT tell the user exactly
			if maxIndex==fApple:           # what the pet wants when he/she feeds it.
				foodPref="Apple"           # It just gives the user and idea of what it
			elif maxIndex==fBlueberry:     # may like.
				foodPref="Blueberry"
			else:
				foodPref="Grape"
			print string.center("Food Preference: "+foodPref, 30)
			
			sum=0 #generate random food choice based on preferences
			for c in food:
				sum+=c
			foodChoice=random.uniform(0,sum)
			if foodChoice<food[fApple]:
				hungry("Apple")
			elif foodChoice<(food[fApple]+food[fBlueberry]):
				hungry("Blueberry")
			else:
				hungry("Grape")
			percent[EAT]+=24
			x+=1 # update counter for food preference
		elif event == 'p': # poop event
			didPoop=needToPoop()
			if didPoop:
				percent[POOP]+=22
			else:
				print "Oh no! You were too slow in taking him to the washroom!"
		elif event == 'z': # sleep event
			didSleep=needToSleep()
			if didSleep:
				percent[SLEEP]+=22
			else:
				print "Oh no! You were too slow in putting your pet to sleep!"
		elif event == 'f': # playing fetch with the pet
			fetch()
			percent[FETCH]+=23
		elif event == 's': # saving
			save()
			print "File for " + name + " saved successfully!"
		elif event == 'x': # exiting the program
			sure=raw_input("Are you sure? Unsaved progress will be lost. ('y'/'n'): ")
			while sure != 'y' and sure != 'n':
				print "Invalid input. Please type 'y'-yes or 'n'-no"
				sure=raw_input("Are you sure? Unsaved progress will be lost. ('y'/'n'): ")
				
			if sure=='y':
				break
		else:
			pass
		time.sleep(2)

	for i in range(len(percent)): # caps pet's levels at 100
		if percent[i]>100:
			percent[i]=100
			
	if didIdle: # only decreases pet's levels if it moves/idles
		percent[EAT]-=4
		percent[POOP]-=2
		percent[SLEEP]-=1
		percent[FETCH]-=3
		for i in range(len(percent)): # sets minimum pet levels to 0
			if percent[i]<0:
				percent[i]=0
		h=0
		for i in percent:
			h+=i
		HAPPY=h/int(len(percent)) # calculate happiness at average of levels
		