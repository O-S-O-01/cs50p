# Reformats "last, first" as "first last"
name =input('what is your name? ').strip()

# Checks if the name contains a comma (format "last, first"); if so, it splits the string into last and first name, rearranges it to "first last", and then prints a greeting using the cleaned-up name
if ',' in name:
    last, first = name.split(', ')
    name = f'{first} {last}'
print(f'hello, {name}')
