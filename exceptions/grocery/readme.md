### What this Program Does

---
***it Creates a grocery list asking for user to enters items one per line Counts how many times each item appears
Outputs results in Uppercase and Alphabetical order and Stops on pressing Ctrl+D***

---
### How to Test the program

Run the progam withpython3 grocery.py

- Example Run
    
    Input:

    apple

    banana

    apple

    milk

    banana

    apple

    Ctrl+D

and the output would be

    Output:

    3 APPLE

    2 BANANA

    1 MILK
    
- it is Case Insensitivity

    Input:

    Apple

    APPLE

    apple

- the output would be

    Output:

    3 APPLE

---
>Frequency counting using a dictionary, Use dictionary to track counts (item → count) Update values dynamically Normalize input (lower()) to avoid duplicates Sort keys before output