class Vault:
    # Class that represents wizard money (galleons, sickles, knuts)

    def __init__(self, galleons=0, sickles=0, knuts=0):
        # Runs automatically when a Vault object is created
        # Stores values inside the object
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        # Controls what is printed when print(object) is used
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        # Defines what happens when we use + between two Vault objects
        # self = left object, other = right object

        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts

        # Returns a NEW Vault object with the combined values
        return Vault(galleons, sickles, knuts)


# Create first Vault object (Harry Potter's money)
potter = Vault(100, 50, 25)
print(potter)  # automatically calls __str__()

# Create second Vault object (Weasley money)
weasley = Vault(25, 50, 100)
print(weasley)  # automatically calls __str__()

# Add both Vault objects together
# Python internally does: potter.__add__(weasley)
total = potter + weasley

# Print the combined result
print(total)

# Defines a Vault class that stores wizard money in galleons, sickles, and knuts,
# allows objects to be printed in a readable format using __str__,
# and overloads the + operator using __add__ so two Vault objects can be added together,
# then creates two Vault objects (potter and weasley), prints them, and prints their combined total.