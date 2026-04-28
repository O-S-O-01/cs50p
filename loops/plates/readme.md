### What This Program Does

---

***Validates a license plate based on rules:***
- 2–6 characters
- Starts with 2 letters
- No symbols
- Numbers only at the end
- First number cannot be 0

---
### How to Test the Program

Run the program with python3 plates.py

Examples:

    Plate: CS50 → Valid

    Plate: CS05 → Invalid

    Plate: CS50A → Invalid

    Plate: C → Invalid

>Use multiple condition checks Loop through characters Track when numbers start using a flag (number_started)