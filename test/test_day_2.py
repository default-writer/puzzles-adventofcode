from src.day_2 import validate, validate2

from .utils import get_lines_data

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
    lines = get_lines_data("/test/data/day_2")
    valid_counter = 0

    for line in lines:
        if validate(line):
            valid_counter += 1

    assert valid_counter == 500

def test_day_2_part2():
    lines = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""".split("\n")
    valid_counter = 0
    for line in lines:
        if validate2(line):
            valid_counter += 1

    assert valid_counter == 1

def test_day_2_dataset_part2():
    lines = get_lines_data("/test/data/day_2")
    valid_counter = 0
    for line in lines:
        if validate2(line):
            valid_counter += 1

    assert valid_counter == 313