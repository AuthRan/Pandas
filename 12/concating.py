'''
Concating data frames : 
It means concatting data row wise or column wise

pd.concate([df1, df2], axis = 0, ignore_index = True)

axis : 0 means row wise concatinate or 1 means coulumn wise concatinate
ignore_index : true means reset indexes of new data frame that is being created
'''

import pandas as pd

df1 = pd.DataFrame({
    "CustomerId" : [1, 2],
    "Name" : ["Ashu", "Yash"]
})

df2 = pd.DataFrame({
    "CustomerId" : [3, 4],
    "Name" : ["Sourav", "Tirth"]
})

# Concatinate vertically axis = 0

concat_data = pd.concat([df1,df2], axis=0, ignore_index=True)

print(concat_data)