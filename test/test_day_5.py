from src.day_5 import get_maximum_seat_index, get_your_seat_index

from .utils import get_raw_data

def test_day_5_part1():
    lines="""BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""
    lines = lines.split("\n")
    index = get_maximum_seat_index(lines)
    assert index == 820

def test_day_5_dataset_part1():
    lines = get_raw_data("/test/data/day_5")
    lines = lines.split("\n")
    index = get_maximum_seat_index(lines)
    assert index == 874

def test_day_5_part2():
    lines="""BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""
    lines = lines.split("\n")
    index = get_your_seat_index(lines)
    assert index == None

def test_day_5_dataset_part2():
    lines = get_raw_data("/test/data/day_5")
    lines = lines.split("\n")
    index = get_your_seat_index(lines)
    assert index == 279
