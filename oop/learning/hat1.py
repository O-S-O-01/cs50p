# Defines a Hat class with a class-level list of houses, then uses a @classmethod so the sort method belongs to the class itself (not an instance), allowing it to randomly assign a house to a given name using cls.houses, and finally calls the method directly on the class without creating an object.
import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
         print(name, "is in", random.choice(cls.houses))
	
Hat.sort("Harry")

