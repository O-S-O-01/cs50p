# The program runs main(), which calls get_student() to collect a name and house from the user, returns them directly as a dictionary with keys "name" and "house", stores that dictionary in student, and then prints the stored values by accessing them using student['name'] and student['house'].
# Eliminates unneeded variable

def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {'name':name, 'house': house}

if __name__=='__main__':
    main()