import re

name = input("What's your name? ").strip()

# Uses regex to match a "last, first" name format, allowing optional spaces due to the * after the comma, then swaps the captured groups to print the name as "first last"
matches = re.search(r'^(.+), *(.+)$', name)

if matches:
    name= matches.group(2) + ' ' + matches.group(1)
print (f' hello, {name} ')
