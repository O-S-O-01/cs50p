# Replaces character [a-zA-Z0-9_] class with \w
import re

email= input("What's your email? ").strip()

# Uses regex ^\w+@\w+\.edu$ where \w is shorthand for letters, numbers, and underscores, so it works like [a-zA-Z0-9_] but is shorter and cleaner
if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")