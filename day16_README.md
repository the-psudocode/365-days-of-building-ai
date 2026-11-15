# Day 16 – Multiple Linear Regression Model Training and Integration

## Objective

Train a Multiple Linear Regression model using student academic data, evaluate its performance, save the trained model, and integrate it into the Streamlit application.

## Work Completed

1. Loaded the prepared training and testing datasets using Pandas.
2. Separated input features and target variable.
3. Trained a Multiple Linear Regression model using Scikit-learn.
4. Examined the model intercept and feature coefficients.
5. Generated predictions using unseen test data.
6. Evaluated model performance using MAE, MSE, and R².
7. Saved the trained model using Pickle.
8. Loaded the saved model into the Streamlit application.
9. Connected the student input form to the trained model.
10. Generated predictions directly through the application interface.

## Model Features

- Study hours
- Attendance
- Previous score
- Sleep hours
- Assignment completion

**Target:** Final student score.

## Model Evaluation

| Metric                    |  Result |
| ------------------------- | ------: |
| Mean Absolute Error (MAE) |  2.1361 |
| Mean Squared Error (MSE)  | 10.6270 |
| R² Score                  |  0.9782 |

Note: The dataset contains only 20 synthetic student records. These evaluation results are preliminary and do not establish real-world predictive performance.

## Model Prediction Example

For a sample student with:

- Study hours: 4
- Attendance: 75%
- Previous score: 60
- Sleep hours: 7
- Assignment completion: 80%

\*\*Predicted final score: 69.
