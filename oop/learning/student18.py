# Moves get_student into Student class
# Defines a Student class that stores a student's name and house, includes a __str__ method to format how the object is printed, and uses a @classmethod called get to collect user input and create a Student object using cls(name, house), then in main() the class method is called directly using Student.get() to create a student and print the result.
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()