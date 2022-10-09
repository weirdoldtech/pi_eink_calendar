#!/usr/bin/python
# -*- coding:utf-8 -*-

from __future__ import print_function
from datetime import datetime
import os.path
import dateutil

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from dateutil.parser import parse as dtparse
from datetime import datetime as dt


# This sets the format of the date display
dateDisplayFormat = '%d %B'  
# %d: Returns the day of the month, from 1 to 31.
# %m: Returns the month of the year, from 1 to 12.
# %Y: Returns the year in four-digit format (Year with century). like, 2021.
# %y: Reurns year in two-digit format (year without century). like, 19, 20, 21
# %A: Returns the full name of the weekday. Like, Monday, Tuesday
# %a: Returns the short name of the weekday (First three character.). Like, Mon, Tue
# %B: Returns the full name of the month. Like, June, March
# %b: Returns the short name of the month (First three character.). Like, Mar, Jun
# %H: Returns the hour. from 01 to 23.
# %I: Returns the hour in 12-hours format. from 01 to 12.
# %M: Returns the minute, from 00 to 59.
# %S: Returns the second, from 00 to 59.
# %f: Return the microseconds from 000000 to 999999
# %p: Return time in AM/PM format
# %c: Returns a locale’s appropriate date and time representation
# %x: Returns a locale’s appropriate date representation
# %X: Returns a locale’s appropriate time representation
# %z: Return the UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).
# %Z: Return the Time zone name (empty string if the object is naive).
# %j: Returns the day of the year from 01 to 366
# %w: Returns weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
# %U: Returns the week number of the year (Sunday as the first day of the week) from 00 to 53
# %W: Returns the week number of the year (Monday as the first day of the week) from 00 to 53
 

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

import shutil

# destStr is the filepath you want to save to, can be a network location.
destStr = "C:/PythonExamples/Output/todoList.txt"

# my_file is the local file called todoList.txt which will initially be written.
my_file = open("todoList.txt", "w")

# by writing this, if it can't connect to google calendar, this will be the only text in the file
# which is useful, so the display python program on the pi can show something alternative if it see's this.
my_file.write("Can't connect to calendar")

my_file = open("todoList.txt", "w")
import sys
import os

import logging
import calendar

import time

import traceback

x = datetime.now()
lastupdated = x.strftime("%A") + " " + x.strftime("%d") + " " + x.strftime("%B")
lastupdated
my_file.write(lastupdated + "\n")
#Google Calendar Events
creds = None

if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('calendar', 'v3', credentials=creds)

# Call the Calendar API
now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
# Insert Calendar ID from Google Calendar in calendarId on following line
#calenderToUse = 'ITWILLBEAVERYLONGSTRINGOFNUMBERSANDLETTERSANDYOUCANFINDITINYOURCALENDARSSETTINGSONGOOGLECALENDER@group.calendar.google.com'
calenderToUse = 'primary'
events_result = service.events().list(calendarId=calenderToUse, timeMin=now,
                                    maxResults=8, singleEvents=True,
                                    orderBy='startTime').execute()
events = events_result.get('items', [])

starty = 60
if not events:
    print('No upcoming events found.')
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))

    eventDay = dt.strftime(dtparse(start), format=dateDisplayFormat)

    if len(event['summary']) >= 25:
        shortEvent = event['summary'][0:22] + "..."
    else:
        shortEvent = event['summary']
    eventText = eventDay + " - " + shortEvent
    my_file.write(eventText + "\n")
    print(eventText)

exit = 1

my_file.close()


shutil.copy("todoList.txt",destStr)
print ("ALL OK!")
