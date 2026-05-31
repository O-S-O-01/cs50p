import re
url = input("URL: ").strip()
	
# Uses regex with a strict character class ([a-z0-9_]+) to capture only valid Twitter usernames after "twitter.com/", allowing optional http/https and www, and uses the walrus operator to assign and check the match in one step
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
