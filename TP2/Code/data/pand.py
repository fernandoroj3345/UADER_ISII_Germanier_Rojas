import pandas as pd
import msvcrt
df = pd.read_csv("dataset.csv", index_col="id")
print(df)
print()
print(df.describe())
print()
print(df.head())
print()
print(df.tail())
print()
msvcrt.getch()
