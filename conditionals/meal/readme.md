### What This Program Does

---
***This program asks for a time in 24-hour format (HH:MM) and determines if it is:***
- breakfast time (7:00–8:00)
- lunch time (12:00–13:00)
- dinner time (18:00–19:00)

*If it’s not within these ranges, it outputs nothing.*

### How to Test the Program

***Run the program with python meal.py***
- Expected Outputs:
                    7:30    → breakfast time
                    12:15   → lunch time
                    18:45   → dinner time
- No Output if time is:
                        10:00
                        
                        15:00

                        21:00
---
> The program converts time into a numeric value and checks if it falls within specific ranges.