# Validates email address by checking whether domain ends with .edu
email = input("What's your email? ").strip()

username, domain = email.split("@")

#the .endswith method checks if the domain variable end with .edu
if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("invalid")