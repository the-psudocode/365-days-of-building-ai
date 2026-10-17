from sklearn.linear_model import LinearRegression

model = LinearRegression()

# Training data

study_hours = [[1], [2], [3], [4], [5]]
scores = [20, 30, 40, 50, 60]

model.fit(study_hours, scores)

print("Study hours:", study_hours)
print("Student scores:", scores)

prediction = model.predict([[8]])

print("Predicted score for 6 study hours:", prediction[0])

print("Learned slope:", model.coef_[0])
print("Learned intercept:", model.intercept_)

predictions = model.predict(study_hours)

print("Model predictions:", predictions)