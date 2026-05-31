# Defines a Student class and creates a student object, assigns name and house as attributes using dot notation, then returns the object so main() can print them in the format "name from house".
class Student:

    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")    
    return student

if __name__ == "__main__":
    main()
