# Validates email address by checking for @ with regex
import re

email = input ('what is your email?').strip()

# Checks if the email contains an "@" symbol using regex search; returns True if found, otherwise False
if re.search ('@', email):
    print('valid')
else:
    print('invalid')