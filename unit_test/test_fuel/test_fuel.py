from fuel import convert, gauge
import pytest


def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("0/1") == 0
    assert convert("1/1") == 100


def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ValueError):
        convert("-1/4")
    with pytest.raises(ValueError):
        convert("1/-4")

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
