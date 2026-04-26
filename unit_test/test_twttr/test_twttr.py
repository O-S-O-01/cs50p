import twttr
from twttr import shorten


def test_lowercase():
    assert shorten("twitter") == "twttr"


def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"


def test_mixed_case():
    assert shorten("TwItTeR") == "TwtTR"


def test_no_vowels():
    assert shorten("rhythm") == "rhythm"


def test_all_vowels():
    assert shorten("aeiou") == ""


def test_numbers_symbols():
    assert shorten("123!@#") == "123!@#"
