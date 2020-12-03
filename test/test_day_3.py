
from src.day_3 import get_tree_counter

from .utils import get_raw_data

def test_day_3_part1():
    lines = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".split("\n")
    tree_counter = get_tree_counter(lines, 3, 1)
    assert tree_counter == 7

def test_day_3_dataset_part1():
    lines = get_raw_data("/test/data/day_3")
    tree_counter = get_tree_counter(lines, 3, 1)
    assert tree_counter == 193

def test_day_3_part2():
    lines = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".split("\n")
    tree_counter = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for slope in slopes:
        tree_counter *= get_tree_counter(lines, slope[0], slope[1])
    assert tree_counter == 336

def test_day_3_part2():
    lines = get_raw_data("/test/data/day_3")
    tree_counter = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for slope in slopes:
        tree_counter *= get_tree_counter(lines, slope[0], slope[1])
    assert tree_counter == 1355323200
