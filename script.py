import numpy as np
import csv

def load(file_name):
    with open(file_name, 'rt') as f:
        reader = csv.reader(f)



    return reader

reader = load("Datasets/winequality-red.csv")

list = np.array([])

for index, data in reader:



