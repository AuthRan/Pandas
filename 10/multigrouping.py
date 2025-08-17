import pandas as pd

data={
    "Name" : ["Arun", "Simran", "Anjhisht", "Karun", "Ashu"],
    "Age" : [21,30,15,15, 21],
    "Salary" : [1000, 500, 200, 800, 100]
}

df = pd.DataFrame(data)

grouped = df.groupby(["Age", "Name"])["Salary"].sum()

# Same age ke log with their names are grouped together

print(grouped)