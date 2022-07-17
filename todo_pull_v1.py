#!/usr/bin/python
# -*- coding:utf-8 -*-

from __future__ import print_function
#import datetime
from datetime import datetime
import os.path

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

import shutil

# destStr is the filepath you want to save to in a network place.
destStr = "\\SOMENETWORKFOLDER"

# my_file is the local file called todoList.txt which will initially be written.
my_file = open("todoList.txt", "w")

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
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
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
print('Getting the upcoming 10 events')
# Insert Calendar ID from Google Calendar in calendarId on following line
events_result = service.events().list(calendarId='CALENDARID@group.calendar.google.com', timeMin=now,
                                    maxResults=8, singleEvents=True,
                                    orderBy='startTime').execute()
events = events_result.get('items', [])

starty = 60
if not events:
    print('No upcoming events found.')
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    startDate = event['start'].get('date')
    if startDate != None:
        eventDay = datetime.strptime(startDate, '%Y-%m-%d')
    else:
        startDate = "Huh?"
    if len(event['summary']) >= 25:
        shortEvent = event['summary'][0:22] + "..."
    else:
        shortEvent = event['summary']
    print (shortEvent)
    eventText = eventDay.strftime('%a %d') + " - " + shortEvent
    my_file.write(eventText + "\n")
    print(eventText)

exit = 1

my_file.close()

print (destStr)
shutil.copy("todoList.txt",destStr)
