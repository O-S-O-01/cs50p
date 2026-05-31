### What the code does
Validates license plates using rules:
- 2–6 characters
- first two must be letters
- numbers only allowed at the end
- first number cannot be 0
- only letters and numbers allowed

### How to test
- `pytest test_plates.py`
- Test:
  - valid plates → `"CS50"`, `"ABC123"`
  - invalid length → `"A"`, `"ABCDEFG"`
  - invalid start → `"1ABC"`
  - invalid symbols → `"CS50!"`
  - invalid number placement → `"CS5A"`
  - leading zero → `"CS01"`

### Key idea
Validation logic = rule-by-rule testing:
- each rule should have at least one test case
- think in terms of “what should fail and why”
