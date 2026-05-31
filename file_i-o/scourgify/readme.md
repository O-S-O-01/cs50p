### What the code does
Reads a CSV file containing names in `"last, first"` format and writes a new CSV with separate `first`, `last`, and `house` columns.

### How to test
- `python scourgify.py before.csv after.csv`
- open `after.csv` to confirm names split correctly

### Key idea
Use:
- `csv.DictReader()` for reading
- `split(", ")` to separate names
- `csv.DictWriter()` for writing cleaned data
