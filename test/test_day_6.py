from src.day_6 import get_counter_for_group, get_counter_for_group2

from .utils import get_line_groups

def test_day_6_part1():
    input = """abc

a
b
c

ab
ac

a
a
a
a

b"""
    def get_sample_line_groups(input):
        line_groups = input.split("\n\n")
        for line_group in line_groups:
            yield line_group.split("\n")
    counter = 0
    for group in get_sample_line_groups(input):
        counter += get_counter_for_group(group)
    assert counter == 11

def test_day_6_dataset_part1():
    counter = 0
    for group in get_line_groups('/test/data/day_6'):
        counter += get_counter_for_group(group)
    assert counter == 7128

def test_day_6_part2():
    input = """abc

a
b
c

ab
ac

a
a
a
a

b"""
    def get_sample_line_groups(input):
        line_groups = input.split("\n\n")
        for line_group in line_groups:
            yield line_group.split("\n")
    counter = 0
    for group in get_sample_line_groups(input):
        counter += get_counter_for_group2(group)
    assert counter == 6

def test_day_6_dataset_part2():
    counter = 0
    for group in get_line_groups('/test/data/day_6'):
        counter += get_counter_for_group2(group)
    assert counter == 3640
