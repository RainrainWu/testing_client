from hypothesis import given
from hypothesis.strategies import integers

from app import fizzbuzz


@given(integers())
def test_fizzbuzz(i):
    if i % 15 == 0:
        assert fizzbuzz(i) == 'fizzbuzz'
    elif i % 5 == 0:
        assert fizzbuzz(i) == 'buzz'
    elif i % 3 == 0:
        assert fizzbuzz(i) == 'fizz'
    else:
        assert fizzbuzz(i) == str(i)
