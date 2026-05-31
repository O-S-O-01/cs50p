import re

email= input('what is your email? ').strip()

# Uses regex ^[^@]+@[^@]+\.edu$ to ensure the email has characters before and after "@", ends with ".edu", and does not allow extra "@" symbols, making it more precise than .+ patterns
#[^@]+ means any character except an @. 
# [^@]+\.edu means any character except an @ followed by an expression ending in .edu. 
if re.search(r'^[^@]+@[^@]+\.edu$', email):
    print('valid')
else:
    print('invalid')