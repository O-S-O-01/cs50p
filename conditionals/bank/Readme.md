### What This Program Does ###
---
*This program asks the user for a greeting and assigns it a monetary value as a a tip which would be given to the banker*:

- [] Outputs $0 if the greeting starts with hello
- [] Outputs $20 if the greeting starts with h (but not hello)
- [] Outputs $100 otherwise

*The check is case-insensitive and ignores leading spaces.*

### How to Test the Program ###

- Run the program: with python3 bank.py

+ Should Output $0 as tip for banker replies like hello, Hello dear, hello customer.

+ Should Output $20 for banker replies like hi,hey, How are you .

+ Should Output $100 for banker replies like,good morning, what's up, customer .
 ---

==The program cleans the input (removes spaces and ignores case) and checks how the greeting starts using string matching.==