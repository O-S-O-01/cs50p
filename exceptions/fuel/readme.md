### What the Program Does

---
***this program Prompts the user for a fraction in the form X/Y*** 

***it converts it to a percentage, and displays:***

    "E" if the tank is almost empty (≤ 1%)

    "F" if the tank is almost full (≥ 99%)

    Otherwise, prints the percentage

The program keeps asking until valid input is provided.

---
### How to Test the program

Run the program with python3 fuel.py

- Valid Inputs Input: like  3/4 should Output: 75%

- Input: 1/100 should Output: E

- Input: 99/100 should Output: F

- Invalid Inputs like

        Input: 5/0

        Input: 10/5

        Input: cat/dog
(should reprompt)

---
>Input validation with loops + exception handling Keep asking until input is valid (while True), Use try/except to handle errors safely Convert and process only after validation