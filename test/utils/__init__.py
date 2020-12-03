import os
from os import remove, truncate

def get_data(file):
    with open(file= os.getcwd() + file, mode="r") as data:
       return [int(line[:-1]) for line in data.readlines()]
            
def iterator(values):
    def iter(dict, number):
        for value in values:
            if value < number:
                if value not in dict.keys():
                    dict[value] = number - value
                    yield value
            continue
    return iter