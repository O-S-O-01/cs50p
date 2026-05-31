# Stores student as (mutable) list
# Stores the student's name and house in a mutable list so the house can be changed later using indexing if the student's name is "Padma".
def main():
        student = get_student()
        if student[0] == "Padma":
                student[1] = "Ravenclaw"
        print(f"{student[0]} from {student[1]}")
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]

if __name__ == "__main__":
    main()