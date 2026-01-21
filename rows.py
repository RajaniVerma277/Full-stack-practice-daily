#head   #tail

# print('display')
# print(df.head(10))
# print(df.tail(10))

# 1-number of rows and column
# 2-column NameError
# non null count
# memory usage
#shape and column
# print(df.describe())


import pandas as pd
df = pd.read_json("sample_Data.json")
# print(df.shape)
# print(df.columns)
# print(df["name"])
subset = df[["name","description","price"]]
print(subset)