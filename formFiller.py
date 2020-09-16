'''
This is an early version of the PHS Auto Attendance Script
Just specify your info in the file config.txt
Entry IDs are HARDCODED. They will become more flexible in the future by smartly searching for more data entry fields.
'''

import requests
import webbrowser
import os

# Parses the URL from the given command line arguments. Not very useful at the moment, but when the script becomes more flexible for other forms, it will.

url = "https://docs.google.com/forms/d/e/1FAIpQLSckymPmvHPzYxhNx6hgD-dR-WETt7eD3S4JzD4rm7TafINZjg/formResponse"

user_data = []

# with open(os.path.realpath('config.txt'), 'r') as config:
with open(('config.txt'), 'r') as config:
    user_data = config.read().splitlines()

user_data = [data.strip() for data in user_data]  # ensure no leading/trailing spaces in data

if len(user_data) != 4:  # data doesn't have 3 lines
    print('There was an error reading from the config file. Please ensure that the file contains your first name, last name, and grade number on 3 separate lines.')
else:
    grade_levels = {
        '9': 'Grade 9',
        '10': 'Grade 10',
        '11': 'Grade 11',
        '12': 'Grade 12',
    }

    # Dictionary of all the entry values
    # Test entries: entry.2005620554 , entry.1624489572 , entry.839337160
    # Real entries: entry.37835231 , entry.477309531 , entry.793669177
    submissions = {
        'emailAddress': user_data[0],
        'entry.1657521344': user_data[1],
        'entry.502163738': user_data[2],
        'entry.1429504230': grade_levels[user_data[3]],
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