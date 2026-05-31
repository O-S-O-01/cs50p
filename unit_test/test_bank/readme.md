### What the code does
Returns a value based on greeting:
- `0` → starts with `"hello"`
- `20` → starts with `"h"` but not `"hello"`
- `100` → all other greetings

### How to test
- `pytest test_bank.py`
- Test:
  - `"hello"` → 0
  - `"hi"` → 20
  - `"good morning"` → 100
  - case-insensitive inputs → `"Hello"` works
  - edge prefixes like `"hey"` and `"house"`

### Key idea
Rule-based logic testing:
- each condition (hello / h / other) must be tested separately
- focus on behavior categories, not random inputs