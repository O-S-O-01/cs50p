# The program gets a student's name and house from the user using get_student(), stores them in a dictionary, then checks if the student's name is "Padma" and if so changes their house to "Ravenclaw", before printing the updated name and house using dictionary key access.

def main():
    student = get_student()
    if student["name"] == 'Padma':
        student['house'] = 'Ravenclaw'
    print(f'{student['name']} from {student['house']}' )

def get_student():
    name = input('Name: ')
    house = input ('house: ')
    return{'name':name, 'house':house}

if __name__ == '__main__':
    main()