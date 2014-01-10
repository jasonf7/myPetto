## Authors: Jason Fang, Zuqi Li, Jesse Jie, Andrew Zhou, Eric Pei
## Jake Si
## Date: November 27, 2013
## Subject: SE101
## Description: This file is used to generate the RGB values of the food cards used for the robot.
## It is only used to set up the robot and should not ever be ran by the user.

from myro import *

init("COM4")

setLED("left", "off")
setLED("right", "off")
setLED("front", "off")
setLED("back", "off")

f_name = "food.txt"

food = raw_input("Food: ")

autoCamera()
img = takePicture()
show(img)
raw_input("Press enter when ready...")
pixels = getPixels(img)
r = g = b = 0
for pixel in pixels:
	r_tmp, g_tmp, b_tmp = getRGB(pixel)
	r += r_tmp
	g += g_tmp
	b += b_tmp
r /= getWidth(img) * getHeight(img)
g /= getWidth(img) * getHeight(img)
b /= getWidth(img) * getHeight(img)

f = open(f_name, 'a')
str = food + ' ' + str(r) + ' ' + str(g) + ' ' + str(b) + '\n'
f.write(str)
f.close()
