### What the code does
Reads a CSV pizza menu file and prints it as a formatted table using the tabulate library.

### How to test
- `python pizza.py regular.csv`
- `python pizza.py sicilian.csv`
- `python pizza.py invalid.txt`

### Key idea
Use:
- `csv.reader()` to read CSV
- `tabulate()` to display rows as a grid table