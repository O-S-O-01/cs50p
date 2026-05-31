import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command line arguments")

    regular = sys.argv[1]

    if not  regular.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open( regular) as file:
            reader = csv.reader(file)

            rows = list(reader)   # convert all rows into a list

    except FileNotFoundError:
        sys.exit("File does not exist")

    # First row = headers
    headers = rows[0]

    # Remaining rows = table data
    table = rows[1:]

    print(tabulate(table, headers, tablefmt="grid"))


if __name__ == "__main__":
    main()