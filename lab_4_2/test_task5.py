import pytest
from task5 import combine_dicts

@pytest.mark.parametrize("d1, d2, expected", [
    ({"a": 1}, {"b": 2}, {"a": 1, "b": 2}),  # Разные ключи
    ({"a": 1, "b": 2}, {"b": 3, "c": 4}, {"a": 1, "b": 3, "c": 4}),  # Пересечение ключей
    ({}, {"x": 10}, {"x": 10}),  # Пустой первый
    ({"y": 20}, {}, {"y": 20}),  # Пустой второй
    ({}, {}, {})  # Оба пустые
])
def test_combine_dicts(d1, d2, expected):
    assert combine_dicts(d1, d2) == expected
    