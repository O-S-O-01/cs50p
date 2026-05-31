url = input('URL: ').strip()

# Uses the string method removeprefix() to remove "https://twitter.com/" from the URL if it exists, leaving only the username portion to be printed
username = url.removeprefix("https://twitter.com/")
print(f"Username: {username}")