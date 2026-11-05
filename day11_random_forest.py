
from sklearn.ensemble import RandomForestClassifier

# Training data
# Study hours
X = [[1], [2], [3], [4], [5],
     [6], [7], [8], [9], [10]]

# 0 = Fail, 1 = Pass
y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

# Create the Random Forest model
model = RandomForestClassifier(
    n_estimators=10,
    random_state=42
)

# Train the model
model.fit(X, y)

# Predict for a new student
study_hours = [[3.5]]

prediction = model.predict(study_hours)

# Display prediction
if prediction[0] == 1:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")


# Get predictions from individual trees
print("\nIndividual Tree Predictions:")

votes = []

for i, tree in enumerate(model.estimators_):
    tree_prediction = tree.predict(study_hours)[0]
    votes.append(int(tree_prediction))

    result = "Pass" if tree_prediction == 1 else "Fail"

    print(f"Tree {i + 1}: {result}")

# Count votes
pass_votes = votes.count(1)
fail_votes = votes.count(0)

print("\nPass Votes:", pass_votes)
print("Fail Votes:", fail_votes)

# Final prediction
print("Final Prediction:",
      "Pass" if pass_votes > fail_votes else "Fail")

# Check prediction probabilities
probabilities = model.predict_proba(study_hours)

print("\nPrediction Probabilities:")
print("Fail Probability:", probabilities[0][0])
print("Pass Probability:", probabilities[0][1])
