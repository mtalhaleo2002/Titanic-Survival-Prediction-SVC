
# DigiSkills 3.0 - Artificial Intelligence Using Python
# Hands-on Exercise No. 02
# Task 2: Data Exploration

import pandas as pd

# Load Titanic dataset
df = pd.read_csv("data/titanic.csv")

print("=" * 65)
print("TASK 2: DATA EXPLORATION")
print("=" * 65)

# Step 1: Numerical descriptive statistics
print("\n1. DESCRIPTIVE STATISTICS")
print("-" * 65)

print(df.describe().to_string())

# Step 2: Identify numerical variables
print("\n2. NUMERICAL VARIABLES")
print("-" * 65)

numerical_columns = df.select_dtypes(
    include=["number"]
).columns.tolist()

print(numerical_columns)

# Step 3: Identify categorical variables
print("\n3. CATEGORICAL VARIABLES")
print("-" * 65)

categorical_columns = df.select_dtypes(
    include=["object", "category"]
).columns.tolist()

print(categorical_columns)

# Step 4: Analyze Sex column
print("\n4. SEX - UNIQUE VALUES")
print("-" * 65)

print(df["Sex"].unique())

print("\nSEX - FREQUENCY DISTRIBUTION")
print(df["Sex"].value_counts().to_string())

# Step 5: Analyze passenger class
print("\n5. PASSENGER CLASS - UNIQUE VALUES")
print("-" * 65)

print(df["Pclass"].unique())

print("\nPASSENGER CLASS - FREQUENCY DISTRIBUTION")
print(df["Pclass"].value_counts().sort_index().to_string())

print("\nTask 2 Completed Successfully!")
