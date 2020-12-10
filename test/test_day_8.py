from src.day_8 import get_program, fix_program, execute

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
    program = get_program(input)
    memory = {}
    registers = {}
    execute(program, memory, registers)
    assert registers["ax"] == 5

def test_day_8_dataset_part1():
    input = get_raw_data("/test/data/day_8")
    program = get_program(input)
    memory = {}
    registers = {}
    execute(program, memory, registers)
    assert registers["ax"] == 1766

def test_day_8_part2():
    input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
    program = get_program(input)
    registers = fix_program(program)
    assert registers == 8

def test_day_8_dataset_part2():
    input = get_raw_data("/test/data/day_8")
    program = get_program(input)
    ax = fix_program(program)
    assert ax == 1639