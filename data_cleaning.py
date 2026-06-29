import pandas as pd

df = pd.read_csv("dirty_data.csv")

print("Original Dataset:")
print(df)
print("\n")

df_no_null = df.dropna()
print("After Removing Null Values:")
print(df_no_null)
print("\n")

df_clean = df_no_null.drop_duplicates()
print("Final Cleaned Dataset (No Nulls & No Duplicates):")
print(df_clean)