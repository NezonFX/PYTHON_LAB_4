import pytest
from task3 import is_palindrome

@pytest.mark.parametrize("value, expected", [
    ("шалаш", True),
    ("А роза упала на лапу Азора", False), 
    ("Анна", True), 
    (12321, True),
    (12345, False),
    ("", True),
    ("a", True)
])
def test_is_palindrome(value, expected):
    assert is_palindrome(value) == expected