
# Day 5: Visualizing Machine Learning Data

import matplotlib.pyplot as plt

# Training data
study_hours = [1, 2, 3, 4, 5]
scores = [20, 30, 40, 50, 60]

print("Study hours:", study_hours)
print("Student scores:", scores)


# Create a scatter plot

plt.scatter(study_hours, scores, label="Student data")
plt.plot(study_hours, scores, marker="o", linestyle="--", label="Trend line")
plt.grid(True)
plt.legend()


# Add labels and title
plt.xlabel("Study Hours")
plt.ylabel("Student Score")
plt.title("Study Hours vs Student Scores")

# Display the graph
plt.show()
