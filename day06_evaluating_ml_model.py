from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

study_hours = [[1],[2],[3],[4],[5]]
scores = [20, 30, 40, 50, 60]

model = LinearRegression()

model.fit(study_hours, scores)

predictions = model.predict(study_hours)

error = mean_absolute_error(scores, predictions)

print("Actual Scores:", scores)
print("Predicted SCores:", predictions)
print("Mean Absolute Error:", round(error, 2))