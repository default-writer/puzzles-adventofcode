from os import environ

from src.day_1 import fix_report

from .utils import get_data

def test_fix_report():
    lines = "1721 979 366 299 675 1456".split()
    result = fix_report(2020,lines)
    assert result == 514579

def test_fix_report_day_1():
    lines = get_data("/test/data/day_1")
    result = fix_report(2020,lines)
    assert result == 956091
