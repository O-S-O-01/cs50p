import re

email = input('what is your email? ').strip()

# Uses regex .+@.+\.edu to check that the email has text before and after "@", and ends with ".edu", making it stricter than the previous patterns
#r".+@.+\.edu" tells Python to treat backslashes (\) as literal characters, not special Python escape characters.
if re.search(r'.+@.+\.edu', email):
    print('valid')
else:
    print('invalid')