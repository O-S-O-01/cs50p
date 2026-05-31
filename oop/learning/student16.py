class Student:
    # Class definition: creates a blueprint for Student objects
    def __init__(self, name, house):
        # Runs automatically when a Student object is created

        if not name:
            # Validation: ensures name is not empty
            raise ValueError('invalid name')

        # This triggers the house.setter method (not direct assignment)
        self.name = name
        self.house = house

    def __str__(self):
        # Controls how the object is printed with print(student)
        return f'{self.name} from {self.house}'


    # PROPERTY: getter method (runs when you access student.house)
    # Getter for house
    @property
    def house(self):
        # Returns the actual stored value
        return self._house


    # SETTER: runs when you assign student.house = value
    # Setter for house
    @house.setter
    def house(self, house):

        # Validation rule for allowed houses
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError('Invalid house')

        # Stores the value in a private variable (_house)
        self._house = house


def main():
    # Starts the program
    student = get_student()

    # Prints student using __str__ method automatically
    print(student)


def get_student():
    # Collect user input
    name = input('name: ')
    house = input('house: ')

    # Creates Student object (triggers __init__)
    return Student(name, house)


if __name__ == '__main__':
    # Ensures main() runs only when file is executed directly
    main()