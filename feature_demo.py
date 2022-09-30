#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os

libdir = '/home/pi/e-Paper/RaspberryPi&JetsonNano/python/lib'

if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in5_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd7in5_V2 Demo")

    epd = epd7in5_V2.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    font28 = ImageFont.truetype('/home/pi/project_todo/pic/Inconsolata-Regular.ttf', 28)

    Himage = Image.new('1', (epd.width, epd.height), 255)
    draw = ImageDraw.Draw(Himage)
    draw.text((10, 0), 'hello tech friends', font = font28, fill = 0)   
    draw.line((20, 50, 70, 100), fill = 0)
    draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
    draw.rectangle((80, 50, 130, 100), fill = 0)
    draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
    imageToUse = Image.open('/home/pi/project_todo/wot_logo.png')
    Himage.paste(imageToUse,(330,0))
    epd.display(epd.getbuffer(Himage))
    time.sleep(2)

    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in5.epdconfig.module_exit()
    exit()
