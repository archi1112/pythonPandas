"""
1.1D array - Series
2.2D array - Dataframe
3.reading csv file
4.shape-returns rows and cols
5.info
6.describe
7.value_counts
8.count
9.column selection using brackets or dot operator
10.loc v/s iloc
11.at v/s iat
12.add/ remove columns
13.inserting column at particular col
14 . add / remove rows - (concat , append , iloc(apply same using loc)
"""
import pandas as pd

# 1:Series(1D Array)
basicList = [1, 2, 3]
pandaSeries = pd.Series(basicList)

# 2:Dataframe : 2D Array
# 3: Reading csv file
df = pd.read_csv("C:/Users/agolia/Desktop/employee.csv")
print(df)

# 4 : shape
print(df.shape)

# print first 3 rows and last 3 rows
print(df.head(3))
print(df.tail(3))

# 5 : prints summary
print("Information : ", df.info())

# 6 : prints the stats
print("Print all the stats :", df.describe())

# 7. set any column as index
df.set_index("ID" , inplace=True)

# 8 : prints count of values
print(df['Department'].value_counts())

# 9 : prints the nonnull values
print(df.count())

# 10. Accessing the columns
# using dot operator
print(df.Name)

# using brackets (Columns having space in their names can be accessed using only brackets and not dot operator)
print(df['Salary'])

# 11 . loc v/s iloc
# loc - access group of rows/cols by labels [inclusive , inclusive]
print("Printing names")
# print the name column using loc [inclusive , exclusive ]
print(df.loc[:,'Name'])

# print from id 2 to 5 all cols(2 is exclusive and 5 is inclusive)
print(df.iloc[2:5,:])


# 12 removing columns
# df.drop('Salary', axis=1, inplace=True)
# print(df)

# 13 .  adding / removing rows

# ignore index is used to remove the default indexes of previous dataframes and create new
print(pd.concat([df,df], ignore_index=True))

# pandaSeries=pandaSeries.append(pandaSeries , ignore_index=True)
# print("combined panda series : \n" , pandaSeries)


df.iloc[1]=['yosh','IT' ,50000]
print(df)

# removing the rows
# index gets started from 2 since 0,1 removed , so reset index
df.drop([1,2] , inplace=True)
# drop=True to drop the original index
# reset_index won't work since already set id as index'
# df.reset_index(drop=True)

print("After deleting and resetting index : \n " ,df)

# dropping rows with certain condition
x=df[df['Salary']>80000]
print(df.drop(x.index , inplace=True))
print("Deleted employees with salary > 80000 \n" , df)
