# Changes * to +
import re

email = input('what is your name ? ').strip()

# Uses the regex pattern .+@.+ to check that the email has at least one character before and after "@", making it stricter than just checking for "@" alone
if re.search('.+@.+',email):
    print('valid')
else:
    print('invalid')