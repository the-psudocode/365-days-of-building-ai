from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

X = [[1], [2], [3], [4], [5],
     [6], [7], [8], [9], [10]]

y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

model = DecisionTreeClassifier(random_state=42)

model.fit(X, y)

study_hours = [[3.5]]

# Predict for a new student
study_hours = [[3.5]]

prediction = model.predict(study_hours)

if prediction[0] == 1:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")

plt.figure(figsize=(10, 6))

tree.plot_tree(
    model,
    feature_names=["Study Hours"],
    class_names=["Fail", "Pass"],
    filled=True
)

plt.title("Student Pass/Fail Decision Tree")
plt.show()