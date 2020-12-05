
from src.day_4 import get_passport_validation_info, get_passport_validation_info2

from .utils import get_raw_data

import logging

logger = logging.getLogger(__name__)

def test_day_4_part1():
    lines = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""
    counter = 0
    for line in lines.split("\n\n"):
        tags = {}
        is_valid, error = get_passport_validation_info(line, tags)
        if is_valid:
            counter += 1
            print(f"VALID {counter} {line}")
        else:
            print(f"INVALID {error}: {line}")
    assert counter == 2


def test_day_4_dataset_part1():
    lines = get_raw_data("/test/data/day_4")
    counter = 0
    for line in lines.split("\n\n"):
        tags = {}
        is_valid, error = get_passport_validation_info(line, tags)
        if is_valid:
            counter += 1
            print(f"VALID {counter} {line}")
        else:
            print(f"INVALID {error}: {line}")
    assert counter == 239

def test_day_4_part2():
    lines = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""
    counter = 0
    for line in lines.split("\n\n"):
        line = line.replace(" "," ")
        line = line.replace("\t"," ")
        line = line.replace("\n"," ")
        is_valid, error = get_passport_validation_info2(line)
        if is_valid:
            counter += 1
            print(f"VALID {counter} {line}")
        else:
            print(f"INVALID {error}: {line}")

    assert counter == 2

def test_day_4_dataset_part2():
    lines = get_raw_data("/test/data/day_4")
    counter = 0
    for line in lines.split("\n\n"):
        is_valid, error = get_passport_validation_info2(line)
        if is_valid:
            counter += 1
            print(f"VALID {counter} {line}")
        else:
            print(f"INVALID {error}: {line}")
    assert counter == 188