import pandas as pd

data = {
    "Name" : ["Ashutosh", "Soumya", "Yash", "Sourav"],
    "Age" : ["21", "23", "19", "30"],
    "City" : ["Ravangla", "Pune", "Sacundrabad", "Asansol"]
}

# df = pd.DataFrame(data)
# print(df)

# df.to_csv("Output.csv", index=False)

df = pd.DataFrame(data)
print(df)

# df.to_excel("Output.xlsx", index=False)
df.to_json("Output.json", index=False)