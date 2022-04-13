import pandas as pd
df = pd.read_csv("dataset.csv", index_col="id")
print(df)
df.describe()
df.head()
df.tail()