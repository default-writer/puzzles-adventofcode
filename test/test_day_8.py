from src.day_8 import get_program, get_accumulator_value

from .utils import get_raw_data

def test_day_8_part1():
    input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
    program = []
    program = get_program(input, program)
    accumulator = get_accumulator_value(program)
    assert accumulator == 5

def test_day_8_dataset_part1():
    input = get_raw_data('/test/data/day_8')
    pass

def test_day_8_part2():
    input = """"""
    pass

def test_day_8_dataset_part2():
    input = """"""
    pass