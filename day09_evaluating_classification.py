
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Training data
X = [[1], [2], [3], [4], [5],
     [6], [7], [8], [9], [10]]

# 0 = Fail, 1 = Pass
y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create the model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Predict using test data
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)

print("Actual Results:", y_test)
print("Predicted Results:", y_pred)
print("Accuracy:", accuracy * 100, "%")

# Confusion Matrix
matrix = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:")
print(matrix)
