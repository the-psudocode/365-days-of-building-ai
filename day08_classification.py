from sklearn.linear_model import LogisticRegression

X = [[1],[2],[3],[4],[5],[6]]
y = [0, 0, 0, 1, 1, 1]

model = LogisticRegression()
model.fit(X,y)

# Create and train the model
model = LogisticRegression()
model.fit(X, y)

# Predict for a student studying 3.5 hours
study_hours = [[3.5]]

prediction = model.predict(study_hours)
probabilities = model.predict_proba(study_hours)

# Display prediction
if prediction[0] == 1:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")

# Display probabilities
print("Fail Probability:", probabilities[0][0])
print("Pass Probability:", probabilities[0][1])

# Test different study hours
students = [[1], [2], [3], [4], [5], [6]]

for student in students:
    result = model.predict([student])
    probability = model.predict_proba([student])

    print("Study Hours:", student[0])
    print("Prediction:", "Pass" if result[0] == 1 else "Fail")
    print("Pass Probability:", round(probability[0][1] * 100, 2), "%")
    print("-------------------")
