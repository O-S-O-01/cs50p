import re

url =input('URL: ').strip()

# Uses re.sub() with a regex pattern to remove optional "http:// or https://", optional "www.", and the "twitter.com/" domain from the start of the URL, leaving only the username part
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")

#Notice how the ^ caret was added to the url. Notice also how the . could be interpreted improperly by the interpreter. Therefore, we escape it using a \ to make it \. For the purpose of tolerating both http and https, we add a ? to the end of https?, making the s optional. Further, to accommodate www we add (www\.)? to our code. Finally, just in case the user decides to leave out the protocol altogether, the http:// or https:// is made optional using (https?://).