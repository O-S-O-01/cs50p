
import re
email = input("What's your email? ").strip()

# Uses regex ^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$ to allow only letters, numbers, and underscores before and after "@", making it stricter than [^@]+ by limiting valid characters
# [a-zA-Z0-9_] tell the validation that charater must be between a-z, A-Z, 0-9 and may include an underscore,

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print ('valid')
else:
    print('invalid')
