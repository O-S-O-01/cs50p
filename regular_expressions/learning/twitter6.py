import re

url = input("URL: ").strip()

# Uses regex with a non-capturing group (?:www\.) to optionally match "www.", then captures the username part after "twitter.com/" and prints it using the walrus operator to assign and check the match in one step
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))


#Notice that the ?: tells the interpreter it does not have to capture what is in that spot in our regular expression.
