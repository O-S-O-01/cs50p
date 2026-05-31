# Implements sort() with an instance method
# Creates a Hat class that stores a list of Hogwarts houses, then defines a sort method that takes a student's name and randomly assigns one of the houses using random.choice, and finally creates a Hat object and sorts "Harry" into a random house.
import random
class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))

# hat = Hat() instantiates a hat that is Hat class is the design for building the object hat, where Hat() is building something from that design
# Think of a blueprint for a house: Blueprint = class Hat, Building a house = Hat(), Building a house = Hat()
hat = Hat()
hat.sort('Harry')      


