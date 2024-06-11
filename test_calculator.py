import pytest
from calculator import sum, minus, multiplication, divide

def test_sum():
    assert sum(1, 2) == 3

def test_minus():
    assert minus(2, 1) == 1

def test_multiplication():
    assert multiplication(2, 3) == 6

def test_divide():
    assert divide(6, 2) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
