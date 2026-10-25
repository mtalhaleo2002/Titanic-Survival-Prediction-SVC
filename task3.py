
# DigiSkills 3.0 - Artificial Intelligence Using Python
# Hands-on Exercise No. 02
# Task 3: Data Cleaning

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "titanic.csv")

print("=" * 65)
print("TASK 3: DATA CLEANING")
print("=" * 65)

# Step 1: Count missing values
print("\n1. MISSING VALUES BEFORE CLEANING")
print("-" * 65)
print(df.isnull().sum().to_string())

print("\nTotal Missing Values:", df.isnull().sum().sum())

# Step 2: Fill numerical columns using median
# Only actual predictor columns are considered here.
numeric_columns = ["Age", "Fare", "SibSp", "Parch"]

for col in numeric_columns:
    median_value = df[col].median()

    print(f"\n{col} Median: {median_value:.2f}")

    df[col] = df[col].fillna(median_value)

# Step 3: Fill categorical columns using mode
categorical_columns = ["Sex", "Embarked"]

for col in categorical_columns:
    mode_value = df[col].mode(dropna=True)[0]
    df[col] = df[col].fillna(mode_value)

# Cabin has many missing values.
# Fill missing values with an explicit category.
df["Cabin"] = df["Cabin"].fillna("Unknown")

# Name and Ticket are retained as text fields.
for col in ["Name", "Ticket"]:
    df[col] = df[col].fillna("Unknown")

# Step 4: Verify missing values
print("\n2. MISSING VALUES AFTER CLEANING")
print("-" * 65)
print(df.isnull().sum().to_string())

remaining = df.isnull().sum().sum()
print("\nTotal Remaining Missing Values:", remaining)

if remaining != 0:
    raise ValueError("Missing values still exist!")

# Step 5: Save cleaned dataset
cleaned_file = DATA_DIR / "titanic_cleaned.csv"

df.to_csv(cleaned_file, index=False)

print("\nCleaned dataset saved:", cleaned_file)
print("Dataset Shape:", df.shape)
print("\nTask 3 Completed Successfully!")
