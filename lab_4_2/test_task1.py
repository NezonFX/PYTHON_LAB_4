import pytest
from task1 import count_words

@pytest.mark.parametrize("sentence, expected", [
    ("Привет мир", 2),
    ("  Много   пробелов   между  словами ", 4),
    ("Одно", 1),
    ("", 0),
    ("     ", 0),
])
def test_count_words(sentence, expected):
    assert count_words(sentence) == expected