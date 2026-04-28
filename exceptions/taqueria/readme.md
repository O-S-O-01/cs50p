### What This Program Does

---
***Simulates a food ordering system:***
- User enters menu items one at a time Program adds up the total cost
- Displays the running total after each valid item
- Ignores invalid items Stops when user presses Ctrl+D

---
### How to Test the Program
Run the program with python3 taqueria.py

    - Item: burrito

    $7.50

    - Item: taco

    $10.50

    - Item: nachos

    $21.50

- Invalid Input (ignored)

    - Item: pizza

- Stop Input
Ctrl + D

---
***this are the list of available item***
    ***"Baja Taco" "Burrito" "Bowl" 
    "Nachos" "Quesadilla" "Super Burrito" "Super Quesadilla" "Taco" "Tortilla Salad"***

>Using a dictionary for lookup + running total, Store menu as dict (item --> price), Check if item exists before using it Accumulate values over time (total += price) Handle continuous input with EOFError
 
 