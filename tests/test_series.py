from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series



def test_version():
    actual = __version__
    expected = '0.1.0'
    assert actual == expected
# ------------------------------
def test_fibonacci_zero():
    actual = fibonacci(0)
    expected= 0
    assert actual ==expected


def test_fibonacci_one():
    actual = fibonacci(1)
    expected= 1
    assert actual ==expected

def test_fibonacci_two():
    actual = fibonacci(2)
    expected= 1
    assert actual ==expected
# ------------------------------

def test_lucas_zero():
    actual = lucas(0)
    expected= 2
    assert actual ==expected


def test_lucas_one():
    actual = lucas(1)
    expected= 1
    assert actual ==expected

def test_lucas_two():
    actual = lucas(2)
    expected= 3
    assert actual ==expected
# --------------------------------
def test_sum_six():
    actual = sum_series(6)
    expected = 8
    assert actual == expected

def test_sum_two_lucas():
    actual = sum_series(2, 2, 1)
    expected = 3
    assert actual == expected

def test_sum_two_fibonacci():
    actual = sum_series(2, 0, 1)
    expected = 1
    assert actual == expected
