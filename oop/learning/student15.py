# Defines a Student class that validates name and house during object creation, stores them as attributes, and formats output using __str__; however in main() a Student object is created and then its house attribute is manually changed to an invalid value ("Number Four, Privet Drive"), bypassing the validation in __init__, and then the object is printed using the __str__ method.
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    student.house = "Number Four, Privet Drive"
    print(student)

def get_student():
    name = input('Name: ')
    house = input('House: ')
    return Student(name, house)

if __name__ == '__main__':
    main()