
# DigiSkills 3.0 - Artificial Intelligence Using Python
# Hands-on Exercise No. 02
# Task 5: Data Visualization

from pathlib import Path
import pandas as pd
import matplotlib

# Use non-interactive backend for automatic image generation
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(BASE_DIR / "data" / "titanic_cleaned.csv")

sns.set_theme(style="whitegrid")

print("=" * 65)
print("TASK 5: DATA VISUALIZATION")
print("=" * 65)

# -----------------------------------------
# GRAPH 1: Gender, Passenger Class, Survival
# -----------------------------------------

print("\n1. Gender, Class and Survival Analysis")

survival_rates = (
    df.groupby(["Pclass", "Sex"])["Survived"]
    .mean()
    .reset_index()
)

survival_rates["Survival_Rate"] = (
    survival_rates["Survived"] * 100
)

print(survival_rates.to_string(index=False))

plt.figure(figsize=(10, 6))

ax = sns.barplot(
    data=survival_rates,
    x="Pclass",
    y="Survival_Rate",
    hue="Sex",
    palette="Set2"
)

ax.set_title(
    "Survival Rate by Gender and Passenger Class",
    fontsize=15
)

ax.set_xlabel("Passenger Class")
ax.set_ylabel("Survival Rate (%)")
ax.set_ylim(0, 110)

plt.legend(title="Gender")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "task5_graph1.png",
    dpi=180,
    bbox_inches="tight"
)

plt.close()

print("Graph 1 generated successfully!")

# -----------------------------------------
# GRAPH 2: Fare Distribution
# -----------------------------------------

print("\n2. Fare Distribution Analysis")

print("Mean Fare:", round(df["Fare"].mean(), 2))
print("Median Fare:", round(df["Fare"].median(), 2))
print("Maximum Fare:", round(df["Fare"].max(), 2))
print("Fare Skewness:", round(df["Fare"].skew(), 2))

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x="Fare",
    bins=35,
    kde=True,
    color="steelblue"
)

plt.title("Distribution of Titanic Passenger Fares")
plt.xlabel("Passenger Fare")
plt.ylabel("Number of Passengers")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "task5_graph2.png",
    dpi=180,
    bbox_inches="tight"
)

plt.close()

print("Graph 2 generated successfully!")

# -----------------------------------------
# GRAPH 3: Survival Comparison by Gender
# -----------------------------------------

print("\n3. Male and Female Survival Comparison")

gender_counts = pd.crosstab(
    df["Sex"],
    df["Survived"]
)

print("\nSurvival Counts:")
print(gender_counts.to_string())

gender_rates = df.groupby("Sex")["Survived"].mean() * 100

print("\nGender Survival Rates (%):")
print(gender_rates.round(2).to_string())

ax = gender_counts.plot(
    kind="bar",
    stacked=False,
    figsize=(10, 6),
    color=["salmon", "mediumseagreen"]
)

ax.set_title("Survival vs Non-Survival by Gender")
ax.set_xlabel("Gender")
ax.set_ylabel("Passenger Count")

plt.xticks(rotation=0)
plt.legend(["Did Not Survive", "Survived"])
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "task5_graph3.png",
    dpi=180,
    bbox_inches="tight"
)

plt.close()

print("Graph 3 generated successfully!")

# -----------------------------------------
# FINAL ANALYSIS
# -----------------------------------------

print("\n4. FINAL ANALYSIS")
print("-" * 65)

highest_gender = gender_rates.idxmax()

print(
    f"Higher observed survival rate: {highest_gender}"
)

fare_skewness = df["Fare"].skew()

if fare_skewness > 1:
    print(
        "Fare distribution is strongly right-skewed."
    )
elif fare_skewness > 0:
    print(
        "Fare distribution is moderately right-skewed."
    )
else:
    print(
        "Fare distribution is not positively skewed."
    )

print("\nAll three graphs saved to output folder.")
print("Task 5 Completed Successfully!")
