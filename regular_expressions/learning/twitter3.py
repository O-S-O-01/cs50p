import re
url = input('URL: ').strip()

# Uses re.sub() to replace the fixed string "https://twitter.com/" in the URL with an empty string, effectively extracting only the username part
username = re.sub(r"https://twitter.com/", '', url)
print(f"Username: {username}")