'''

This is an early version of the PHS Auto Attendance Script
Just specify in the arguments below your name and grade level.
Run the task in your command line using: python formFiller.py -u "https://docs.google.com/forms/d/e/1FAIpQLSfpe6jz-GIykefd3TOQ0pax7-PxsJWRaCrivZFOnkijA43seA/formResponse"

'''

import requests
import webbrowser
import os

# Parses the URL from the given command line arguments. Not very useful at the moment, but when the script becomes more flexible for other forms, it will.

url = "https://docs.google.com/forms/d/e/1FAIpQLSfpe6jz-GIykefd3TOQ0pax7-PxsJWRaCrivZFOnkijA43seA/formResponse"

'''

Entry IDs are HARDCODED. They will become more flexible in the future by smartly searching for more data entry fields.

Please make sure that for the grade level entry, the entry is CASE SENSITIVE. They must be written as formatted: Freshman | Sophomore | Junior | Senior

'''
user_data = []

with open('file://' + os.path.realpath("config.txt"),"r") as config:
	for line in config:
		user_data.append(line)
	
grade_levels = {
"9":"Freshman",
"10":"Sophomore",
"11":"Junior",
"12":"Senior",
}

#Dictionary of all the entry values

submissions = {
"entry.37835231":user_data[0], 
"entry.477309531":user_data[1],
"entry.793669177":grade_levels.get(user_data[2])
}

# Initiates a POST to the server
x = requests.post(url,data=submissions)

# Prints the status of the operation.
if response == '<Response [200]>':
    print('Success')
else:
    print('Failure')

	# success splash screen
webbrowser.open('file://' + os.path.realpath("success.html"))

