# Adds ^ and $ to regex
import re

email = input('what is your email? ').strip()

# ^ means start of string, $ means end of string
# Uses regex ^.+@.+\.edu$ to ensure the entire email starts with text, contains "@", and ends exactly with ".edu", making it stricter by matching the whole string
if re.search(r'^.+@.+\.edu$',email):
    print ('valid')
else:
    print('invalid')
    