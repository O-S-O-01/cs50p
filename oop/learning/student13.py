# Defines a Student class that validates input, stores a student's name, house, and patronus as attributes, uses __str__ to control how the object is displayed, creates a Student object from user input, and prints a formatted description of the student.
class Student:
    def __init__(self, name,house,patronus):
        if not name:
            raise ValueError('missing name')
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

#When asked to convert this object to a string, use this code, and self will refer to the object being converted."
#__str__ is a special built-in method that Python looks for when it needs a string representation of an object
#defines a special method __str__ that returns a string in the format "{self.name} from {self.house}"
    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    #when you write 'print(student)'Python automatically calls:'student.__str__()' which returns:'f"{self.name} from {self.house}"'
    print(student)

def get_student():
    name = input('Name: ')
    house = input('House: ')
    patronus = input('Patronus: ')
    return Student(name, house, patronus)

if __name__ =='__main__':
    main()
