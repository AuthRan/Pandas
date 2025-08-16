# To read data in a fixed amount use .head(n) -> By default 5 or .tail(n) -> By default 5
import pandas as pd

df = pd.read_json("../sample_Data.json")

print("Upr ke 5 rows")
print(df.head())  # By default will read five line