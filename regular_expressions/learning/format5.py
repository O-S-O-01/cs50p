import re

name = input("What's your name? ").strip()

# Uses the walrus operator (:=) to assign and check the regex match in one step, then swaps "last, first" into "first last" before printing a greeting
if matches := re.search(r'^(.+), *(.+)$', name):
    name = matches.group(2) + ' ' + matches.group(1)
print(f'hello {name}')