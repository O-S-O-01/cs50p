# Defines a Student class that validates a student's name, house, and optional patronus, stores them as object attributes, provides a __str__ method for displaying the student as text, includes a charm method that returns an emoji based on the student's patronus, creates a Student object from user input, and prints the corresponding Patronus charm.
class Student:
    def __init__(self, name, house, patronus=None):
        if not name:
            raise ValueError('missing name')
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        
        
    # The parameter patronus=None above allows the value to be optional, while "patronus = input('Patronus: ') or None" in def get_student ensures that if the user enters nothing, patronus becomes None; therefore the condition "if patronus and patronus not in [...]" only validates the input when a patronus was actually provided, skipping validation when it is None.
    # The "patronus=None" makes patronus optional, and "patronus = input('Patronus: ') or None" converts an empty input into None, so the condition "if patronus and patronus not in [...]" ensures no error is raised when patronus is empty (None), but raises a ValueError only when a patronus is provided and it is not in the allowed list.
        if patronus and patronus not in ["Stag", "Otter", "Jack Russell terrier"]:
            raise ValueError("Invalid patronus")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    
    
    #This is called a method. A method is simply a function that belongs to a class.
        def charm(self):
        
            #The match statement is a control flow statement that allows you to compare a value with multiple patterns and execute code based on the first matching pattern.
         #The case statements define the patterns to match against. The underscore _ is a wildcard that matches any value.
         #The return statements specify what to return for each matching case.

        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🎉"
def main():
    student = get_student()
    print ("Expecto Patronum!")
    
    #student.charm() calls the charm method on the student object, which returns an emoji based on the student's patronus, and print() displays the returned emoji.
    print (student.charm())

def get_student():
    name = input('Name: ')
    house = input('house: ')
    patronus = input('Patronus: ') or None  
    return Student(name, house, patronus)

if __name__ =='__main__':
    main()
