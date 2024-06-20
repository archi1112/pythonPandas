import numpy as np
import pandas as pd

"""
Group by
1.Split - split similar data in groups
2.apply - apply some operation on particular group
3.combine - combine the results

# for all these steps we can directly use groupby function
"""

d = {'City': ['Ahmedabad', 'Baroda', 'Anand',
              'Ahmedabad', 'Baroda', 'Anand'],
     'Temp': [40, 35, 32, 45, 37, 34],
     'Humidity': [32, 34, 23, 24, 27, 32]}
data = pd.DataFrame(d)
print(data)

# display average temperature
print(data['Temp'].mean())

# display average of temp citywise
grp=data.groupby('City')['Temp'].mean()
print(grp)

# iterate all the groups and print
grp=data.groupby('City')

for key,value in grp:
    print(key)
    print(value)


# display the indices in each group
print(grp.groups)

# display first entry in each group formed

grp=data.groupby('City')
print(grp.first())
# last entry
print(grp.last())

# count number of entries in each group
grp=data.groupby('City')
print(grp.size())

# print a specific group
print(grp.get_group('Baroda'))

# print minimum temperature of each group
print(grp.min())
print(grp.count())

# group wise stats
print(grp.describe())

# splitting data based on city and temperature
grp=data.groupby(['City','Temp'])

for key, value in grp:
    print(key)
    print(value)
    print()