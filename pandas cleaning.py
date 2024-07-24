import pandas as pd

file_path = 'data.csv'
df=pd.read_csv("data.csv")
x = df["Calories"].mode()[0]
print(x)

