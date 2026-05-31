### What this Program Does

---
***Converts dates into ISO format (YYYY-MM-DD).

- Accepts two formats:

    Numeric → 9/8/1636

    Text --> September 8, 1636

Keeps asking until a valid date is entered.

---
### How to Test the program

Run the program with python3 outdated.

- Valid Inputs

    Input: 9/8/1636

    Output: 1636-09-08

    Input: September 8, 1636

    Output: 1636-09-08

- Invalid Inputs  (should reprompt), inputs like.

    Input: 13/40/2020

    Input: Sept 8, 2020

    Input: hello world

> Handling multiple input formats + string parsing Detect format using condition ("/" in input) parse differently depending on formatConvert text (month name) --> number using list Clean input (replace, strip) Format output using leading zeros (:02)