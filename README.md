# pi_eink_calendar
A way to display Google calendar items (or anything) on a waveshare e-ink display using python on a raspberry pi


This code is split into two parts:

1) Connects to Google Calendar and retreives the most recent calendar items and stores them in a text file.
2) Retrives the text file from a network location, and displays the content on the waveshare e-ink display.

I've chosen to run these two parts separately on two different computers, because while testing, when envoking the Google Calendar api steps, I needed to re-validate the user login on occassion. This was difficult on a headless raspberry pi, as there was no GUI to accomplish this. You can remotely connect to it via VNC etc. but it's very slow on a pi zero. Consequently, I've been running the Calendar retrieve steps on a Windows PC via task scheduler, which is always on in my setup. The file is saved on a NAS which both the Windows PC and the raspberry pi can access. Every 30 minutes or so the Calendar items are refreshed, and every 40 minutes or so the raspberry pi gets the latest file and displays it on the e-ink display.

A beautiful diagram to show data flow

Google Calendar -> retrieve Calender.py -> saves file in NAS -> Nas file -> raspberry pi -> e-ink display

For added flair and because I'm a big Poirot fan, I display an image of the Belgian sleuth to increase the chance I'll actually do the task on the board. It also serves to display an error if the file can't be retrieved. Another Piorot!

To Do
==================
-This method only works with 'All Day' Events. Probably not to difficult to implement differently to show events throughout the day.
-There's no way to indicate if a task is complete, it's completely read only. This could be accomplished in a few ways, the text file could be updated with a tag which the display.py ignores if present. There would have to be some user input to do this, up/down/select.
-Maybe you're not a Poirot lover, I think that's on you, but perhaps some other images would be more suitable!
