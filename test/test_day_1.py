from os import environ

from src.day_1 import fix_report, fix_report2

from .utils import get_data, iterator

def test_day_1_part1():
    """
    In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 
    1721 * 299 = 514579, so the correct answer is 514579.
    """
    values = [int(value) for value in "1721 979 366 299 675 1456".split()]
    result = fix_report(2020, values, iterator(values))
    assert result
    assert  result[0] * result[1] == 514579

def test_day_1_dataset_part1():
    values = get_data("/test/data/day_1")
    result = fix_report(2020, values, iterator(values))
    assert result
    assert result[0] * result[1] == 956091


def test_day_1_part2():
    """
    Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them 
    together produces the answer, 241861950.
    """
    values = [int(value) for value in "1721 979 366 299 675 1456".split()]
    result = fix_report2(2020, values, iterator(values))
    assert result
    assert result[0] * result[1] * result[2] == 241861950


def test_day_1_dataset_part2():
    values = get_data("/test/data/day_1")
    result = fix_report2(2020, values, iterator(values))
    assert result
    assert result[0] * result[1] * result[2] == 46767014