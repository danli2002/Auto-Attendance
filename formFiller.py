'''

This is an early version of the PHS Auto Attendance Script
Just specify your info in the file config.txt

Entry IDs are HARDCODED. They will become more flexible in the future by smartly searching for more data entry fields.
'''

import requests
import webbrowser
import os

# Parses the URL from the given command line arguments. Not very useful at the moment, but when the script becomes more flexible for other forms, it will.

url = "https://docs.google.com/forms/d/e/1FAIpQLSfpe6jz-GIykefd3TOQ0pax7-PxsJWRaCrivZFOnkijA43seA/formResponse"

user_data = []

# with open(os.path.realpath('config.txt'), 'r') as config:
with open(('config.txt'), 'r') as config:
    user_data = config.read().splitlines()

user_data = [data.strip() for data in user_data]  # ensure no leading/trailing spaces in data

if len(user_data) != 3:  # data doesn't have 3 lines
    print('There was an error reading from the config file. Please ensure that the file contains your first name, last name, and grade number on 3 separate lines.')
else:
    grade_levels = {
        '9': 'Freshman',
        '10': 'Sophomore',
        '11': 'Junior',
        '12': 'Senior',
    }

    # Dictionary of all the entry values
    # Test entries: entry.2005620554 , entry.1624489572 , entry.839337160
    # Real entries: entry.37835231 , entry.477309531 , entry.793669177
    submissions = {
        'entry.37835231': user_data[0],
        'entry.477309531': user_data[1],
        'entry.793669177': grade_levels[user_data[2]],
    }

    # Initiates a POST to the server
    response = requests.post(url, data=submissions)

    # Prints the status of the operation.
    if response.status_code == 200:
        print('Success')
        # success splash screen
        webbrowser.open('file://' + os.path.realpath('success.html'))
    else:
        print('Failure')
