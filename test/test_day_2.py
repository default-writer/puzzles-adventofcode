
from src.day_2 import validate

from .utils import get_raw_data

def test_day_2_part1():
    lines = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""".split("\n")
    valid_counter = 0
    for line in lines:
        if validate(line):
            valid_counter += 1

    assert valid_counter == 2

def test_day_2_dataset_part1():
    lines = get_raw_data("/test/data/day_2")
    valid_counter = 0

    for line in lines:
        if validate(line):
            valid_counter += 1

    assert valid_counter == 500
