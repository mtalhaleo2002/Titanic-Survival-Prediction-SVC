
# DigiSkills 3.0 - Artificial Intelligence Using Python
# Hands-on Exercise No. 02
# Task 4: Feature Selection and SVC Model

from pathlib import Path
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.svm import SVC

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

BASE_DIR = Path(__file__).resolve().parent

df = pd.read_csv(BASE_DIR / "data" / "titanic.csv")

print("=" * 65)
print("TASK 4: FEATURE SELECTION AND SVC MODEL")
print("=" * 65)

# Step 1: Identify target and independent variables
target = "Survived"

numeric_features = [
    "Age", "Fare", "SibSp", "Parch"
]

categorical_features = [
    "Sex", "Pclass", "Embarked"
]

features = numeric_features + categorical_features

X = df[features]
y = df[target]

if y.isna().any():
    raise ValueError("Target contains missing values!")

print("\n1. TARGET VARIABLE")
print(target)

print("\n2. INDEPENDENT FEATURES")
print(features)

print("\n3. DATASET SHAPES")
print("X shape:", X.shape)
print("y shape:", y.shape)

# Step 2: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\n4. TRAINING AND TESTING DATA")
print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# Step 3: Numerical preprocessing
numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

# Step 4: Categorical preprocessing
categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)

# Step 5: Build Support Vector Classifier
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", SVC(kernel="rbf", C=1.0))
])

# Step 6: Train model
model.fit(X_train, y_train)

print("\n5. MODEL TRAINING")
print("SVC model trained successfully!")

# Step 7: Make predictions
y_pred = model.predict(X_test)

# Step 8: Evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

cm = confusion_matrix(y_test, y_pred, labels=[0, 1])

print("\n6. MODEL EVALUATION")
print("-" * 65)

print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")

print("\n7. CONFUSION MATRIX")
print(cm)

print("\n8. CLASSIFICATION REPORT")
print(classification_report(
    y_test,
    y_pred,
    zero_division=0
))

# Save predictions
predictions = X_test.copy()
predictions["Actual_Survived"] = y_test.values
predictions["Predicted_Survived"] = y_pred

output_dir = BASE_DIR / "output"
output_dir.mkdir(exist_ok=True)

predictions.to_csv(
    output_dir / "task4_predictions.csv",
    index=False
)

print("\nPredictions saved successfully.")
print("\nTask 4 Completed Successfully!")
