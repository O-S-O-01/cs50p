# Adds optional subdomain
import re

email = input("What's your email? ").strip()

# Uses a regex pattern that allows an optional subdomain before the main domain (e.g. "school.harvard.edu") and ensures the email ends with ".edu", while re.IGNORECASE makes the match case-insensitive
# (\w+\.)? communicates to the interpreter that this new expression can be there once or not at all.
if re.search(r'^\w+@(\w+\.)?\w+\.edu$', email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# here is the full expression that one would have to type to ensure that a valid email is inputted:
    # (r'^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$')