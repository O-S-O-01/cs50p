# this code cares about pattern only, Adds .*, which is used to determine if anything is to the left of the email address and if anything is to the right of the email address 
import re

email = input("what's your email? ").strip()

# Uses regex .*@.* to check if "@" exists anywhere in the email, allowing even empty text before or after it
if re.search(".*@.*", email):
    print('valid')
else:
    print('invalid')
 