import pytest
from task2 import find_unique

@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, 3, 2, 4, 1], [3, 4]),
    (["a", "b", "c"], ["a", "b", "c"]),
    ([1, 1, 2, 2, 3, 3], []),
    ([], []),
    ([5, 4, 3, 2, 1, 1], [5, 4, 3, 2]), 
    ([1, "1", 1], ["1"])
])
def test_find_unique(input_list, expected):
    assert find_unique(input_list) == expected