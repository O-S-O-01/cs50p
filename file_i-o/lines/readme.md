### What the code does
Takes a Python file as a command-line argument and counts the number of actual lines of code, excluding blank lines and comments.

### How to test
- `python lines.py`
- `python lines.py hello.py`
- Test with files containing:
  - blank lines
  - comments starting with `#`
  - normal code

### Key idea
Use file reading line by line and filter out:
- blank lines (`strip() == ""`)
- comment lines (`lstrip().startswith("#")`)
