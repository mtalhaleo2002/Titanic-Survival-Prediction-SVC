import pandas as pd

df = pd.read_csv("data/titanic.csv")

print("Dataset loaded successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 7 Rows:")
print(df.head(7).to_string(index=False))