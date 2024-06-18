import pandas as pd

"""
1. skiprows
2.usecols
3.header=None,any number
4.giving column names
5.chunksize
6.isnnull , notnull
"""


def function(x):
    if x % 2 == 0:
        return True
    else:
        return False


# skip rows with functions(remove all the rows with even indexes)
# df = pd.read_csv("C:/Users/agolia/Desktop/employee.csv",skiprows=lambda x: function(x))
# print(df)

# read only certain columns
# df = pd.read_csv("C:/Users/agolia/Desktop/employee.csv", usecols=['Name'])
# print(df)

# to setheader as 1st row
# header=None will give default headers 0,1,2
# df = pd.read_csv("C:/Users/agolia/Desktop/employee.csv", header=None , names=['a','b','c','d'])
# print(df)

# print in chunks of 2 rows
# df = pd.read_csv("C:/Users/agolia/Desktop/employee.csv", chunksize=2)
# for chunk in df:
#     print(chunk)

# na_values= converts the particular value in NaN
df = pd.read_csv("C:/Users/agolia/Desktop/employee.csv")
print(df)
# print sum of null values in all columns
print(df.isnull().sum())
# for checking rowwise
print(df.isnull().sum(axis=1))

# check null values in department column
print(df[df['Department'].isnull()])
