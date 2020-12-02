import os
from os import remove, truncate

def get_data(file):
    with open(file= os.getcwd() + file, mode="r") as data:
       return [line[:-1] for line in data.readlines()]
            