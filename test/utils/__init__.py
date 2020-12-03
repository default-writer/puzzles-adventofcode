import os
from os import remove, truncate
from itertools import accumulate
import operator

def get_int_data(file):
    with open(file= os.getcwd() + file, mode="r") as data:
       return [int(line[:-1]) for line in data.readlines()]

def get_raw_data(file):
    with open(file= os.getcwd() + file, mode="r") as data:
       return [line[:-1] for line in data.readlines()]
            
def iterator(values):
    def iter(dict, number):
        for value in values:
            if value < number:
                if value not in dict.keys():
                    dict[value] = number - value
                    yield value
            continue
    return iter

def multiply(values):
    result = 1
    for value in values:
        result *= value
    return result

def maximum(values):
    return max([multiply([*value]) for value in values])
