import re

name = input("What's your name? ").strip()

# Uses regex to match a "last, first" name format, then extracts the second group (first name) and first group (last name) and swaps them to display the name as "first last"
matches = re.search(r'^(.+), (.+)$', name)

if matches:
    name= matches.group(2) + ' ' + matches.group(1)
print (f' hello, {name} ')
