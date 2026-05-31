import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command line arguments")

    students = sys.argv[1]

    if not students.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(students, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    count = 0

    for line in lines:
        stripped = line.strip()
        if stripped == "":
            continue

        if line.lstrip().startswith("#"):
            continue

        count += 1

    print(count)


if __name__ == "__main__":
    main()
