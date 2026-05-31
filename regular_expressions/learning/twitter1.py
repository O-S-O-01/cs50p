url = input('URL: ').strip()

# Removes the fixed prefix "https://twitter.com/" from the URL with empty space "" using .replace(), leaving only the username part which is then printed
username = url.replace('https://twitter.com/', '')

print(f'username: {username}')
