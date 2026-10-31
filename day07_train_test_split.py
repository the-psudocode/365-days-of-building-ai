from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

study_hours = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
scores = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

X_train, X_test, y_train, y_test = train_test_split(study_hours, scores, test_size = 0.2, random_state = 42)

# Create the model
model = LinearRegression()

# Train the model using training data only
model.fit(X_train, y_train)

# Predict scores for the testing data
predictions = model.predict(X_test)

# Evaluate the model
error = mean_absolute_error(y_test, predictions)

# Display the results
print("Training data:", X_train)
print("Testing data:", X_test)
print("Actual test scores:", y_test)
print("Predicted test scores:", predictions)
print("Mean Absolute Error:", round(error, 2))