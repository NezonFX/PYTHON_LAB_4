import pytest
from task4 import are_anagrams

@pytest.mark.parametrize("a, b, expected", [
    ("кот", "ток", True),
    ("Слово", "Волос", True),
    ("кот", "коты", False),
    ("кот", "пёс", False),
    ("", "", True),
    ("abc", "cba", True)
])
def test_are_anagrams(a, b, expected):
    assert are_anagrams(a, b) == expected