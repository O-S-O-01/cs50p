import re

name = input("What's your name? ").strip()

# Uses regex to detect a "last, first" format and captures last and first name using groups(), then swaps their order to "first last" before printing a formatted greeting
matches = re.search(r'^(.+), (.+)$', name)

if matches:
    last, first = matches.groups()
    name= first + ' ' + last
print (f' hello, {name} ')
