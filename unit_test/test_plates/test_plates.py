import plates
from plates import is_valid


def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("CS50") == True


def test_start_letters():
    assert is_valid("CS50") == True
    assert is_valid("1S50") == False
    assert is_valid("C150") == False


def test_alphanumeric():
    assert is_valid("CS50!") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS50") == True


def test_number_position():
    assert is_valid("CS50") == True
    assert is_valid("CS5A") == False


def test_leading_zero():
    assert is_valid("CS01") == False
    assert is_valid("CS10") == True
