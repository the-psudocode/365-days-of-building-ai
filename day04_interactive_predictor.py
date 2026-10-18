from sklearn.linear_model import LinearRegression

# Training data
study_hours = [[1], [2], [3], [4], [5]]
scores = [20, 30, 40, 50, 60]

# Create and train the model
model = LinearRegression()
model.fit(study_hours, scores)

print("Welcome to the Student Score Predictor!")

hours = float(input("How many hours did you study? "))

print("You entered", hours, "hours.")

prediction = model.predict([[hours]])

print("Based on your study hours, your predicted score is:", prediction[0])