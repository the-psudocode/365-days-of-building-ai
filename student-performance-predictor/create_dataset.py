import pandas as pd

# Manually created student data
data = {
    "study_hours": [
        1, 2, 3, 4, 5,
        6, 2, 7, 3, 8,
        4, 9, 5, 6, 1,
        8, 7, 3, 10, 4
    ],

    "attendance": [
        55, 60, 65, 70, 80,
        85, 50, 90, 68, 95,
        75, 98, 82, 88, 45,
        92, 85, 62, 99, 72
    ],

    "previous_score": [
        40, 45, 50, 55, 65,
        70, 35, 75, 48, 85,
        60, 90, 68, 72, 30,
        88, 80, 52, 95, 58
    ],

    "sleep_hours": [
        5, 6, 6, 7, 7,
        8, 5, 7, 6, 8,
        6, 8, 7, 7, 4,
        8, 7, 5, 8, 6
    ],

    "assignment_completion": [
        40, 50, 55, 65, 75,
        85, 35, 90, 60, 95,
        70, 98, 80, 88, 30,
        92, 85, 55, 100, 68
    ],

    "final_score": [
        35, 42, 48, 58, 68,
        76, 32, 82, 50, 90,
        63, 95, 72, 80, 25,
        91, 84, 45, 98, 60
    ]
}

# Convert dictionary into a DataFrame
df = pd.DataFrame(data)

# Display the dataset
print(df)

print("\nDataset shape:")
print(df.shape)

print("\nFirst five records:")
print(df.head())

# Save dataset as a CSV file
df.to_csv("data/student_data.csv", index=False)

print("\nDataset saved successfully!")


# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check for duplicate records
print("\nDuplicate records:")
print(df.duplicated().sum())

# Statistical summary
print("\nDataset statistics:")
print(df.describe())