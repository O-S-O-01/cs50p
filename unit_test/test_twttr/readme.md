### What the code does
Removes all vowels (A, E, I, O, U) from a string and returns the shortened version.

### How to test
- `pytest test_twttr.py`
- Test with:
  - words with vowels → `"twitter"` → `"twttr"`
  - uppercase input → `"TWITTER"` → `"TWTTR"`
  - no vowels → `"rhythm"` → `"rhythm"`
  - mixed sentences → vowels removed only

### Key idea
Pure function design:
- `shorten()` returns processed string
- `main()` only handles input/output
- testing checks return values, not printed output
