# Demonstrates immutability of tuples, removes parentheses
# https://scifi.stackexchange.com/q/105992
# Demonstrates tuple immutability by showing that values inside a returned tuple cannot be changed using indexing like student[1] = "Ravenclaw".
def main():
        student = get_student()
        if student[0] == "Padma":
                student[1] = "Ravenclaw"
        print(f"{student[0]} from {student[1]}")
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house

if __name__ == "__main__":
    main()
