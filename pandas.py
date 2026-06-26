import pandas as pd

df = pd.read_csv("students.csv")

print("First few rows of the dataset:")
print(df.head(3))