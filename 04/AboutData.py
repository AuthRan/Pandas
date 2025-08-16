import pandas as pd

data = {
    "Name" : ["Ashutosh", "Soumya", "Yash", "Sourav", "Yug", "Satya", "Shiran", "Gaurav"],
    "Age" : [21, 23, 19, 30, 49, 32, 12, 44],
    "City" : ["Ravangla", "Pune", "Sacundrabad", "Asansol", "Delhi", "Mumbai", "Maharastra", "Chennai"]
}

df = pd.DataFrame(data)
print(f"Number of Columns: {df.columns}")
print(f"Shape of table: {df.shape}")