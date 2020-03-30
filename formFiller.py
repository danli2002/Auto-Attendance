'''

This is an early version of the PHS Auto Attendance Script
Just specify in the arguments below your name and grade level.
Run the task in your command line using: python formFiller.py -u "https://docs.google.com/forms/d/e/1FAIpQLSfpe6jz-GIykefd3TOQ0pax7-PxsJWRaCrivZFOnkijA43seA/formResponse"

'''

import requests
import argparse

# Parses the URL from the given command line arguments. Not very useful at the moment, but when the script becomes more flexible for other forms, it will.
ap = argparse.ArgumentParser()
ap.add_argument("-u","--url",required=True,help="Specifies form URL")
args = vars(ap.parse_args())

url = args["url"]

'''

Entry IDs are HARDCODED. They will become more flexible in the future by smartly searching for more data entry fields.

Please make sure that for the grade level entry, the entry is CASE SENSITIVE. They must be written as formatted: Freshman | Sophomore | Junior | Senior

Dictionary of all the entry values

'''

submissions = {
"entry.37835231":"Daniel", 
"entry.477309531":"Li",
"entry.793669177":"Junior"
}

# Initiates a POST to the server
x = requests.post(url,data=submissions)
# Prints the status of the operation. If it returns something like <Response [200]>, then the operation went through successfully.
print(x)
webbrowser.open("https://www.google.com",new=2)


