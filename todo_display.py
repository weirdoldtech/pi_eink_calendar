#!/usr/bin/python
# -*- coding:utf-8 -*-

from __future__ import print_function
#import datetime
from datetime import datetime
import os.path


import sys
import os

libdir = '/home/pi/e-Paper/RaspberryPi&JetsonNano/python/lib'

if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
import calendar
from waveshare_epd import epd7in5_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

import pprint


logging.info("epd7in5_V2 Demo")
epd = epd7in5_V2.EPD()

logging.info("init and Clear")
epd.init()
epd.Clear()

font10 = ImageFont.truetype('/home/pi/project_todo/Inconsolata-Regular.ttf', 10)
font28 = ImageFont.truetype('/home/pi/project_todo/Inconsolata-Regular.ttf', 28)
font36 = ImageFont.truetype('/home/pi/project_todo/Inconsolata-Regular.ttf', 36)

exit = 0
n = 0
#while exit == 0:
now = datetime.now()
current_time = now.strftime("%H:%M")

Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
draw = ImageDraw.Draw(Himage)

draw.text((epd.width-100, 0), "Last updated: " + current_time, font = font10, fill = 0)
errorMode = False
with open("/home/pi/project_todo/todoList.txt", "r") as a_file:
	for line in a_file:
		if line == "Can't connect to calendar":
			errorMode = True
			

starty = 60
first = True
with open("/home/pi/project_todo/todoList.txt", "r") as a_file:
	for line in a_file:
		stripped_line = line.strip()
		if first:
			first = False
		else:
			draw.text((20, starty),stripped_line, font = font28, fill = 0)
			starty += 50

draw.line((5, 50, 780, 50), fill = 0)

x = datetime.now()
titleBar = x.strftime("%A") + " " + x.strftime("%d") + " " + x.strftime("%B")
draw.text((5,5),str(titleBar), font = font36, fill = 0)
if errorMode == False:

	#Image to display if connection worked
	Himage.paste(Image.open('/home/pi/project_todo/ok.png'),(520,150))
	
else:
	draw.text((270,270),"Mon dieu! Cannot connect!", font = font28, fill = 0)
	#Image to display if connection didn't work
	Himage.paste(Image.open('/home/pi/project_todo/cantconnect.png'),(-10,150))

epd.display(epd.getbuffer(Himage))
epd.sleep()
