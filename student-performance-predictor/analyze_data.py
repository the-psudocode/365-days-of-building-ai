# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the student dataset
df = pd.read_csv("data/student_data.csv")

# Display the dataset
print("Student Dataset:")
print(df)

# Display basic information
print("\nDataset Information:")
print(df.info())

plt.scatter(df["study_hours"], df["final_score"])

plt.xlabel("Stduy Hours")
plt.ylabel("Final Score")
plt.title("Study Hours vs Final Score")

plt.show()

# Scatter plot: Attendance vs Final Score

plt.scatter(df["attendance"], df["final_score"])

plt.xlabel("Attendance")
plt.ylabel("Final Score")
plt.title("Attendance vs Final Score")

plt.show()

# Histogram: Final Score Distribution

plt.hist(df["final_score"], bins=5)

plt.xlabel("Final Score")
plt.ylabel("Number of Students")
plt.title("Distribution of Final Scores")

plt.show()

# Correlation Analysis

correlation = df.corr()

print("\nCorrelation Matrix:")
print(correlation)

# Visualize correlation

plt.imshow(correlation, cmap="coolwarm")

plt.colorbar()

plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=90)
plt.yticks(range(len(correlation.columns)), correlation.columns)

plt.title("Feature Correlation")

plt.show()
