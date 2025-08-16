import pandas as pd

# Reading data from differenct file sources
# df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
# df = pd.read_excel("SampleSuperstore.xlsx")
df = pd.read_json("sample_Data.json")
print(df)

# If You have data stored in cloud like google u need to import gcfs