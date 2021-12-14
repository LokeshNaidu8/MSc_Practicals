import pandas
import numpy

file = pandas.read_csv('Datasets/student-mat.csv')
print(file.head())  # Returns only 5 rows or records
print("\n--------------------------\n", file)  # returns all the data


