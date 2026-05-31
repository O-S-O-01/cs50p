# Defines a Student class with an __init__ method to store name and house, takes user input for both values, creates a Student object using them, returns the object, and prints the stored attributes using dot notation.
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
   name = input("Name: ")
   house = input("House: ")
   student = Student(name, house)   
   return student

if __name__ == "__main__":
    main()
