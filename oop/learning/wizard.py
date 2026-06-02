# Defines a base class Wizard that stores a name and validates it, then creates two child classes (Student and Professor) that inherit from Wizard so they automatically get the name attribute and validation, while adding their own extra attributes (house for Student and subject for Professor), and finally creates objects from each class to demonstrate inheritance and shared behavior.
#super or parent class
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...

# child class
class Student(Wizard):
    def __init__(self, name, house):

# This means:“Go to the parent class (Wizard) and run its init” So name validation is reused.
        super().__init__(name)
        self.house = house

    ...

# child class
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...

wizard =  Wizard("albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")

...