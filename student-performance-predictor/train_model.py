import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load training datasets

X_train = pd.read_csv("data/X_train.csv")
y_train = pd.read_csv("data/y_train.csv")

print("Training Features:")
print(X_train.head())

print("\nTraining Target:")
print(y_train.head())

print("\nTraining Data Shape:", X_train.shape)
print("Target Data Shape:", y_train.shape)

# Convert target into a 1D array
y_train = y_train.squeeze()

# Create the Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

print("\nModel training completed successfully!")

# Display model coefficients

print("\nModel Intercept:")
print(model.intercept_)

print("\nModel Coefficients:")

for feature, coefficient in zip(X_train.columns, model.coef_):
    print(feature, ":", coefficient)

# Load testing data
X_test = pd.read_csv("data/X_test.csv")
y_test = pd.read_csv("data/y_test.csv")

# Convert target into 1D array
y_test = y_test.squeeze()

# Make predictions
predictions = model.predict(X_test)

# Compare actual and predicted scores
results = pd.DataFrame({
    "Actual Score": y_test,
    "Predicted Score": predictions
})

print("\nModel Predictions:")
print(results)

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nModel Evaluation:")
print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("R2 Score:", r2)

# Save the trained model
with open("models/student_performance_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nModel saved successfully!")