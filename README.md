# pi_eink_calendar
A way to display Google calendar items (or anything) on a waveshare e-ink display using python on a raspberry pi

Please note: this readme needs a lot of updating, and I promise I'll get around to it, I surely will...so please watch the youtube video instead, because it covers it in a great deal more detail.

Cheers!

This code is split into two parts:

1) todo_pull_v1.py - Connects to Google Calendar and retreives the most recent calendar items and stores them in a text file.
2) todo_display.py Retrives the text file from a network location, and displays the content on the waveshare e-ink display.

I've chosen to run these two parts separately on two different computers, because while testing, when envoking the Google Calendar api steps, I needed to re-validate the user login on occassion. This was difficult on a headless raspberry pi, as there was no GUI to accomplish this. You can remotely connect to it via VNC etc. but it's very slow on a pi zero. Consequently, I've been running the Calendar retrieve steps (todo_pull_v1.py) on a Windows PC via task scheduler, which is always on in my setup. The file is saved on a NAS which both the Windows PC and the raspberry pi can access. Every hour or so the Calendar items are refreshed, and every 40 minutes or so the raspberry pi gets the latest file and displays it on the e-ink display.

A beautiful diagram to show data flow
======================================

Google Calendar -> todo_pull_v1.py -> saves file to todo_pull_v1.py folder -> in NAS -> Nas file -> raspberry pi -> e-ink display

For added flair and because I'm a big Poirot fan, I display an image of the Belgian sleuth to increase the chance I'll actually do the task on the board. It also serves to display an error if the file can't be retrieved. Another Piorot!

Setting Up
==================
First, get python to talk to Google Calendar following this guide:
https://developers.google.com/calendar/api/quickstart/python

You'll essentially be setting up a user to access your calendar so it's important to understand how authorisation works:
https://developers.google.com/calendar/api/guides/auth

When you start out you'll be in a sort of test environment, whereas when you're up and running you want to publish your work so you don't have to keep re-authenticating a user.

Displaying
===================
There are a lot of e-ink displays on the market, waveshare make a lot of them. Depending on the display you use, you'll need drivers, and an example program so you can see how to draw things on the screen. Here's the waveshare one:

https://www.waveshare.com/wiki/Template:Touch_e-Paper_Codes_Description#Testing_demo

You can draw lines, images, text of various sizes and fonts, it's all very versitile.



To Do
==================
-This method only works with 'All Day' Events. Probably not to difficult to implement differently to show events throughout the day.
-There's no way to indicate if a task is complete, it's completely read only. This could be accomplished in a few ways, the text file could be updated with a tag which the display.py ignores if present. There would have to be some user input to do this, up/down/select.
-Maybe you're not a Poirot lover, I think that's on you, but perhaps some other images would be more suitable!
