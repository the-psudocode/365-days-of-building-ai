# Day 11 – Random Forest Classification

## Objective

Learn how Random Forest classification works and how multiple decision trees combine their predictions to make a final decision.

## Concepts Learned

- Random Forest Classification
- Ensemble Learning
- Individual Decision Tree Predictions
- Majority Voting
- Prediction Probabilities using `predict_proba()`

## Implementation

Built a Random Forest classifier using Scikit-learn to predict whether a student would pass or fail based on study hours.

The model was created using:

- `RandomForestClassifier`
- `n_estimators=10`
- `random_state=42`

## Results

For a student studying 3.5 hours:

- Final Prediction: Fail
- Pass Votes: 0
- Fail Votes: 10
- Fail Probability: 1.0
- Pass Probability: 0.0

## Key Takeaway

Random Forest is an ensemble machine learning algorithm that combines multiple decision trees. It uses their collective predictions to produce a final classification, often making it more robust than relying on a single decision tree.

## Tools Used

- Python
- Scikit-learn
- VS Code
- Git and GitHub
