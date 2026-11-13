import pandas as pd
from sklearn.model_selection import train_test_split

# Load the student dataset
df = pd.read_csv("data/student_data.csv")

# Display the dataset
print("Student Dataset:")
print(df.head())

# Display dataset shape
print("\nDataset Shape:")
print(df.shape)

# Separate features and target

X = df.drop("final_score", axis=1)
y = df["final_score"]

print("\nInput Features (X):")
print(X.head())

print("\nTarget Variable (y):")
print(y.head())

# Check missing values

print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records

print("\nDuplicate Records:")
print(df.duplicated().sum())

# Split dataset into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining Features:")
print(X_train)

print("\nTesting Features:")
print(X_test)

print("\nTraining Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)

# Save prepared datasets

X_train.to_csv("data/X_train.csv", index=False)
X_test.to_csv("data/X_test.csv", index=False)

y_train.to_csv("data/y_train.csv", index=False)
y_test.to_csv("data/y_test.csv", index=False)

print("\nPrepared datasets saved successfully!")