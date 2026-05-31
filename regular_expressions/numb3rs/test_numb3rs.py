import pytest
import numb3rs
from numb3rs import validate

def test_valid():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True


def test_out_of_range():
    assert validate("256.0.0.1") == False
    assert validate("512.512.512.512") == False


def test_invalid_format():
    assert validate("cat") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False


def test_leading_zeros():
    assert validate("192.168.001.1") == False