# Defines a Student class with an __init__ method that stores name and house as object attributes, gets user input to create a Student object, returns the object, and prints the stored attributes using dot notation.
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f'{student.name} from {student.house}')

def get_student():
    name = input('Name: ')
    house = input('House: ')
    return Student(name, house)

if __name__ =='__main__':
    main()
