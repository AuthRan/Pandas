# Aggregation involves summary statistics (sum, mean, count)

'''
df.["ColumnName"].mean()
df.["ColumnName"].min()
df.["ColumnName"].max()
df.["ColumnName"].sum()
'''

import pandas as pd

data={
    "Name" : ["Arun", "Simran", "Anjhisht", "Karun"],
    "Age" : [10,30,5,15],
    "Salary" : [1000, 500, 200, 800]
}

df = pd.DataFrame(data)

print(df["Age"].mean())