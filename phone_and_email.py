#!python3
# phone_and_email.py
# author: Ferdous Ahmed Adit
# Date started: 3rd July 2021

"""
Steps that we might have to do for the project

1. Use the pyperclip module to coyp and paste strings.
2. Create two regexes, one for matching phone nubmers and the other for 
   matching email addresses.
3. Find all matches, not just the first match, of both regexes
4. Neatly format the matched strings in to a single string to paste
5. Dispaly some kind of message if not matches were found in the text. 
"""

import re
import pyperclip

'''
phone_regex should match a normal phone number with or without the area code
and the extension for it. Also the sepaator for easy reading number is 
either a - or a whitespace or .
'''
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code (780 | (780}))
    (\s|-|\.)?                      # 780-555 or 780 555 or 780.555 separator
    (\d{3})                         # first 3 digit after area code
    (\s|-|\.)?                      # separator
    (\d{4})                         # last 4 digit
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)               # ignore whitespaces

'''
email_regex should match a normal email address that has a username made out of 
characters, numbers, ./_/%/+,-. Then an @ sign and after that the 
domain name.something. 
'''
# TODO: Test if we can put \D in the front of username so that it is
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # username
    @                               # @ symbol
    [a-zA-Z0-9.-]                   # domain name
    (\.[a-zA-Z]{2,4})               # dot-something
    )''')

# TODO: Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []

for groups in phone_regex.findall(text):  # find the phone numbers

    # CODE TESTING
    print(groups())
    print('\n\n')
    # CODE TESTING END

    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    # area code
    # 3 digit
    # 4 digit

if groups[8] != '':      # if extension is available
    phoneNum += ' x' + groups[8]
matches.append(phoneNum)  # keep the perfectly stitched phone number

for groups in email_regex.findall(text):  # find the email addresses
    matches.append(groups[0])


# TODO: Copy results to the clipboard
