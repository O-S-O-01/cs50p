# Stores the returned name and house inside a tuple called student, then accesses each value using tuple indexing with student[0] for the name and student[1] for the house.
# Returns student as tuple, without unpacking it
def main():
    student = get student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)

if __name__ == "__main__":
    main()
