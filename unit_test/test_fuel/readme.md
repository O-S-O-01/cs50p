## 4. fuel.py

### What the code does
Converts a fraction `"X/Y"` into a percentage and formats output:
- `E` if ≤ 1%
- `F` if ≥ 99%
- otherwise `"Z%"`

Also handles errors:
- `ValueError` → invalid input or X > Y
- `ZeroDivisionError` → Y is 0

### How to test
- `pytest test_fuel.py`
- Test:
  - valid fractions → `"1/2"` → 50
  - edge values → `"0/1"`, `"1/1"`
  - gauge outputs → `0 → "E"`, `100 → "F"`
  - invalid input → `"a/b"` raises ValueError
  - division by zero → `"1/0"` raises ZeroDivisionError

### Key idea
Two-layer testing:
- normal outputs → `assert`
- error cases → `pytest.raises()`
- separate computation (`convert`) from formatting (`gauge`)