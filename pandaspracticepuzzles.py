import re

import pandas as pd
import numpy as np

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# 1. df = # (complete this line of code) , Create a DataFrame df from this dictionary data which has the index labels.
df = pd.DataFrame(data, index=labels)
print(df)

# 2.  Display a summary of the basic information about this DataFrame and its data
# no print method needed for df.info() since it directly prints the information
print("\n\n***********************Displaying summary of basic information : ***********************\n\n")
df.info()

# print animal  , visits where age =2.5
print("\n\n***********************Displaying animal , visit where age=2.5: ***********************\n\n",
      df.loc[df['age'] == 2.5, ['animal','visits']])
# 3. . Return the first 3 rows of the DataFrame df.
print("\n\n***********************First three rows are : ***********************\n\n", df.head(3))

# 4.Select just the 'animal' and 'age' columns from the DataFrame df.
print("\n\n***********************Display only animal and age column ***********************\n\n",
      df[['animal', 'age']])

"""loc"""
# 5. Select the data in rows [3, 4, 8] and in columns ['animal', 'age'].
print("\n\n***********************Display only animal and age column ***********************\n\n",
      df.loc[['d', 'e', 'i'], ['animal', 'age']])

# 6.Select only the rows where the number of visits is greater than 3.
print("\n\n***********************Display only rows with number of visits > 3 ***********************\n\n",
      df[df['visits'] > 3])

# 7.Select the rows where the age is missing, i.e. it is NaN.
print('\n\n***********************Display only rows with missing age***********************\n\n',
      df[df['age'].isnull()])

# 8.Select the rows where the animal is a cat and the age is less than 3.
print('\n\n***********************Display only rows where the animal is a cat and the age is less than 3'
      '***********************\n\n')
print(df[(df['animal'] == "cat") & (df['age'] < 3)])

# 9.Select the rows the age is between 2 and 4 (inclusive).
print('\n\n***********************Display only rows with age between 2 and 4(inclusive)***********************\n\n',
      df[df['age'].between(2, 4, inclusive="both")])

# 10.Select the rows the age is between 2 and 4 (exclusive).
print('\n\n***********************Display only rows with age between 2 and 4 (exclusive)***********************\n\n',
      df[df['age'].between(2, 4, inclusive="neither")])

# 11.Change the age in row 'f' to 1.5.
df.loc['f', 'age'] = 1.5
print("\n\n***********************Display only rows with age between 2 and 4 (exclusive)***********************\n\n")
print(df.loc['f'])

# 12.calculate sum of all visits(total number of visits)
print("\n\nTotal number of visits : \t ", df['visits'].sum())

"""groupby"""
# 13. Calculate the mean age for each different animal in df.
print("\n\nthe mean age for each different animal in df \t", df.groupby('animal')['age'].mean())

# 14.Append a new row 'k' to df with your choice of values for each column. Then delete that row to return the
# original DataFrame.
df.loc['k'] = ['dog', 3, 2, 'yes']
print("\n\n***********************Added new row with index K***********************\n\n")
print(df.loc['k'])
# Dropping back the kth row
df.drop(index='k', inplace=True)
# print(df)

# 15.Count the number of each type of animal in df.
print("\n\n***********************Number of each type of animal in dataframe***********************\n\n")
print(df['animal'].value_counts())

# 16.Sort df first by the values in the 'age' in descending order, then by the value in the 'visits' column in
# ascending order (so row i should be first, and row d should be last).
print("\n\n*********************Sort df in descending order of age and ascending order of visits "
      "***********************\n\n")
print(df.sort_values(by=['age', 'visits'], ascending=[False, True]))

# 17.The 'priority' column contains the values 'yes' and 'no'. Replace this column with a column of boolean values:
# 'yes' should be True and 'no' should be False.
df['priority'] = df['priority'].replace(to_replace=['yes', 'no'], value=['True', 'False'])
print("\n\n***********************After replacing all yes with true and no with false in "
      "priority***********************\n\n", df)

# 18. In the 'animal' column, change the 'snake' entries to 'python'.
print("\n\n***********************Changing all snake entries to python ***********************\n\n")
df['animal'] = df['animal'].replace(to_replace=['snake'], value=['python'])
print(df)

# 19.For each animal type and each number of visits, find the mean age. In other words, each row is an animal,
# each column is a number of visits and the values are the mean ages (hint: use a pivot table).


# dataframes beyond simplicity
"""20. You have a DataFrame df with a column 'A' of integers. For example:

df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
How do you filter out rows which contain the same integer as the row immediately above?

You should be left with a column containing the following values:

1, 2, 3, 4, 5, 6, 7"""

df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
print("\n\n***********************Filter out rows which contain same integer as row immediately above "
      "***********************\n\n")
df = df.drop_duplicates(subset='A')
print(df)

# 21 . How do you count how many unique rows a DataFrame has (i.e. ignore all rows that are duplicates)?
# this returns rows and cols both
print("\n\nNumber of unique values in dataframe: \t", df.nunique())
# to get only unique rows
print("\n\nNumber of unique vales in dataframe rows only \t", len(df.drop_duplicates(subset='A')))

# Data Cleaning
# 21.
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MArid_miLAN', 'landON_StockOlm',
                               'Budapest_PaRis', 'Brussels_landOn'],
                   'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
                   'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
                               '12. Air France', '"Swiss Air"']})
print(df)

# 21A . Some values in the FlightNumber column are missing (they are NaN). These numbers are meant to increase
# by 10 with each row so 10055 and 10075 need to be put in place. Modify df to fill in these missing numbers and make
# the column an integer column (instead of a float column).

# interpolate copies the previous value to next row
print("\n\n***********************Increase all NAN values by 10 from previous row value in column FlightNumber "
      "***********************\n\n")
df['FlightNumber'] = df['FlightNumber'].interpolate().astype('int')
print(df['FlightNumber'])

""" 21B . The From_To column would be better as two separate columns! Split each string on the underscore delimiter _ to 
give a new temporary DataFrame called 'temp' with the correct values. Assign the correct column names 'From' and 'To' 
to this temporary DataFrame."""
print("\n\n***********************Separate each string on _ as delimiter to create new temp column with correct "
      "values  ***********************\n\n")
temp = df['From_To'].str.split('_', expand=True)
temp.columns = ['From', 'To']
print(temp)

# 21B. Notice how the capitalisation of the city names is all mixed up in this temporary DataFrame 'temp'.
# Standardise the strings so that only the first letter is uppercase (e.g. "londON" should become "London".)
temp['From'] = temp['From'].str.capitalize()
temp['To'] = temp['To'].str.capitalize()
print(temp)

# 21C.  Delete the From_To column from df. Delete the From_To column from df and attach the temporary DataFrame
# 'temp' from the previous questions.df and attach the temporary DataFrame from the previous questions.
df = df.drop(columns=['From_To'])
print(df)
#
# df['From']=temp['From']
# df['To']=temp['To']

# better approach
df = df.join(temp)
print(df)

# 21C . In the Airline column, you can see some extra punctuation and symbols have appeared around the airline names.
# Pull out just the airline name. E.g. '(British Airways. )' should become 'British Airways'.
df['Airline'] = df['Airline'].str.extract('([a-zA-Z]+)', expand=False).str.strip()
print(df)
