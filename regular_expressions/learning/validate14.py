# Adds re.IGNORECASE
import re

email= input("What's your email? ").strip()

# Uses re.IGNORECASE to make the regex case-insensitive, so it treats uppercase and lowercase letters the same when matching the email pattern (e.g. .edu and .EDU are both accepted)
if re.search(r'^\w+@\w+\.edu$', email, re.IGNORECASE):
    print('valid')
else:
    print('invalid')