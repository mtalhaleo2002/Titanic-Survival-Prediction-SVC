# DigiSkills 3.0 - Artificial Intelligence Using Python
# Hands-on Exercise No. 02
# Task 1: Dataset Loading and Initial View

import pandas as pd

# Step 1: Load Titanic dataset into a DataFrame
df = pd.read_csv("data/titanic.csv")

# Step 2: Display dataset dimensions
print("=" * 60)
print("TASK 1: DATASET LOADING AND INITIAL VIEW")
print("=" * 60)

print("\nDataset loaded successfully!")

print("\nTotal Number of Rows:", df.shape[0])
print("Total Number of Columns:", df.shape[1])

# Step 3: Display first 7 rows
print("\nFirst 7 Rows of Titanic Dataset:")
print(df.head(7).to_string(index=False))

print("\nTask 1 Completed Successfully!")