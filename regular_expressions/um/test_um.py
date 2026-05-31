from um import count

def test_single_um():
    assert count("um") == 1

def test_multiple_um():
    assert count("um, hello, um") == 2

def test_case_insensitive():
    assert count("Um, um, UM") == 3

def test_substrings():
    assert count("yummy album umbrella") == 0
