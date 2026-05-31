# Validates email address by checking username and domain separately

email = input("What's your email? ").strip()

#this line having two variables (unpacking) means spliting the inputed email where @ exist and asign the first 
#part to username and second part to domain as in paul@yahoo.com, paul = username, yahoo.com=domain
usename, domain = email.split('@')

if username and '.' in domain:
    print("Valid")
else:
     print("Invalid")
     