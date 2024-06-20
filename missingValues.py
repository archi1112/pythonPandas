import numpy as np
import pandas as pd

"""
1.drop the row having any missing value present
2.modifying row to make all values null
3. adding new nan column
4.deleting whole column having null value
method is deprecated
5.method - used to fill null values 
    ->pad/ffill(Top->Bottom)
    ->backfill/bfill(Bottom->Top)
6.replace
"""
df = pd.read_csv("C:/Users/agolia/Desktop/employee.csv")
print(df, end="\n\n")

# delete row having any one na value
print(df.dropna(how='any'))

# modifying a row to make all values null
df.iloc[9] = {'ID': np.NAN, 'Name': np.NAN, 'Department': np.NAN, 'Salary': np.NAN}
print(df)

print("deleting all null row : \n\n ", df.dropna(how='all'))

# adding new nan column
df['Grade']=np.nan
print(df)
# deleting whole column haing null values
print("deleting all null row : \n\n ",df.dropna(how='all' , axis=1))

# keep rows having atleast 1 non-na values / deleting rows with atmost 1 na values
print("deleting all null row : \n\n ",df.dropna( axis=0, thresh=1))

# deleting grade column again
df.drop('Grade', axis=1,  inplace=True)

# fills all the missing values with 0
print("\n\n" , df.fillna(0))

# fill all nan value in salary column with 60k
# print("\n\n" , df.fillna({'Salary':60000}))

# deprecated
# df.fillna(method="ffill")
print(df)

# replace emily clark with emily thomson
df.replace(to_replace=["Emily Clark"] , value="Emily Thomson",inplace=True)
# changing two names
df.replace(['Emma Johnson','Emily Thomson'],'Emmy' , inplace=True)
print(df)

# replace all nan values
print(df.replace(np.nan,'IT'))

# replace all nan values in department with IT and nan in salary with 15000
print(df.replace({'Department': {np.nan:'IT'},'Salary': {np.nan:10000}}))
