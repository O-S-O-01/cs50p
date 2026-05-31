import re

url = input("URL: ").strip()

# Uses regex to validate and parse a Twitter URL, capturing the username part after "twitter.com/" (while allowing optional http/https and www), then prints the username from group(2) if a match is found
matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(2))


