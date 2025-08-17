'''
It is an imp concept acc to which suppose you have a fruit basket then you can group them as apples banana oranges etc and count number of each fruit 
Similarly,
Given a data you can use group by on a column to segregate items then perform aggregation on these items to get meaningful results.

df.groupby("Column_Jispe_Group_banana_Hai")["Column_jispe_kuch_Mathematical_krna"].agg_method()
'''

import pandas as pd

data={
    "Name" : ["Arun", "Simran", "Anjhisht", "Karun", "Ashu"],
    "Age" : [21,30,15,15, 21],
    "Salary" : [1000, 500, 200, 800, 100]
}

df = pd.DataFrame(data)

grouped = df.groupby("Age")["Salary"].sum()

print(grouped)

# df.groupby("Age") -> Three groups 15, 21, 30
# ["Salary"] -> Each group salaries 15 - 200, 800 ; 21 - 1000, 100 etc
# .sum means add each groups salary