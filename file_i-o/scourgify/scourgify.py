import sys
import csv


def main():
    if len(sys.argv) != 3:
        sys.exit("Too few or too many command-line arguments")

    students = reader()
    writer(students)


def reader():
    before = sys.argv[1]

    if not before.endswith(".csv"):
        sys.exit("Not a CSV file")

    students = []

    try:
        with open(before) as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                last, first = row["name"].split(", ")
                house = row["house"]

                students.append({
                    "first": first,
                    "last": last,
                    "house": house
                })

    except FileNotFoundError:
        sys.exit("File does not exist")

    return students


def writer(students):
    after = sys.argv[2]

    with open(after, "w", newline="") as csvfile:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for student in students:
            writer.writerow(student)


if __name__ == "__main__":
    main()