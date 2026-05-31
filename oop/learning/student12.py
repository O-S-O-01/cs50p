# Defines a Student class that validates the name and house inside __init__, raises a ValueError if the name is missing or the house is invalid, creates a Student object from user input, and prints the student's name and house using object attributes.
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError('missing name')
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
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
