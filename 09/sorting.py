# Manlo ek data aaaya and you want to sort them according to alphabatical order
# Sorting Data 1 Column sort_values()
# df.sort_values(by="Column_Name", ascending=True(for asc or false), inplace=True)

import pandas as pd

data={
    "Name" : ["Arun", "Simran", "Anjhisht", "Karun"],
    "Age" : [10,30,5,15],
    "Salary" : [1000, 500, 200, 800]
}

df = pd.DataFrame(data)
print("Orignal Data..........")
print(df)

df.sort_values(by="Age", ascending=False, inplace=True)

print("Edited Data..........")
print(df)


#------------------------------------------
# To taget multiple columns 
df.sort_values(by=["Age", "Salary"], ascending=[False, False], inplace=True)
print("Targetting multiple data.............")
print(df)

#Pehle Age column descending order me sort hoga
# Agar Age same hote hain, tab Salary descending order me sort hoga