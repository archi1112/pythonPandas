# https://www.youtube.com/watch?v=SAFmrTnEHLg
# iterating the dataframe using iterrows takes lot of time to optimise we should use vectorized form
import pandas as pd

import numpy as np

df = pd.DataFrame()
size = 10
df['age'] = np.random.randint(0, 100, size)
df['time_in_bed'] = np.random.randint(0, 9, size)
df['pct_sleeping'] = np.random.rand(size)
df['favorite_food'] = np.random.choice(['pizza', 'burger', 'fries'])
df['hate_food'] = np.random.choice(['broccoli', 'paratha', 'tomato'])

"""
If they were in bed for more than 5 hours AND they were sleeping for more than 50% we give them favorite food
Otherwise give their hate food
if over 90years give their favorite food regardless
"""


def reward_col(row):
    if row['age'] > 90:
        return row['favorite_food']
    if (row['time_in_bed'] > 5) & (row['pct_sleeping'] > 0.2):
        return row['favorite_food']
    return row['hate_food']


# for loop
for index, row in df.iterrows():
    df.loc[index, 'reward'] = reward_col(row)
print(df)

# vectorized form
df['reward'] = df['hate_food']
df.loc[(df["time_in_bed"] > 5) & (df['pct_sleeping'] > 0.2) | (df['age'] > 90), 'reward'] = df['favorite_food']
print(df)
