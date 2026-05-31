import re

email = input ('what is your email? ').strip()

# Uses regex ^\w+@\w.+\.(com|edu|gov|net|org)$ to validate an email with allowed username/domain patterns and restrict the ending to specific domains like .com, .edu, .gov, .net, or .org
# Notice that the | has the impact of an or in our expression.
if re.search(r'^\w+@\w.+\.(com|edu|gov|net|org)$', email):
    print('valid')
else:
    print('invalid')
    