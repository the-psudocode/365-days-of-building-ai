# Day 17 – Student Performance AI: UI Enhancement

## Overview

On Day 17 of the 365 Days of Building AI challenge, I enhanced the Student Performance AI application by improving its user interface and prediction result presentation.

The application uses a trained Multiple Linear Regression model to estimate a student's final academic score based on multiple performance-related factors.

## Objectives

- Improve the AI prediction interface.
- Add student name input and validation.
- Display predicted scores in a clear format.
- Introduce a visual performance indicator.
- Improve the overall user experience.

## Features Implemented

### 1. Student Information Input

Users can enter:

- Student name
- Daily study hours
- Attendance percentage
- Previous examination score
- Daily sleep hours
- Assignment completion percentage

### 2. Machine Learning Prediction

The application uses the previously trained Multiple Linear Regression model to predict the student's expected final score.

### 3. Improved Prediction Display

- Displays the predicted final score using Streamlit metrics.
- Shows a visual progress bar representing the predicted score percentage.
- Displays a success message after prediction.
- Validates the student name before generating a prediction.

### 4. Dashboard Improvements

- Updated dashboard metrics.
- Improved application description.
- Navigation between Dashboard, Student Analysis, and AI Prediction pages.

## Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Pickle

## Concepts Learned

- Streamlit metrics using `st.metric()`
- Progress indicators using `st.progress()`
- Input validation
- Python's `max()` and `min()` functions
- Improving user experience in ML applications
- Integrating a trained ML model with a Streamlit interface

## Project Structure

```text
student-performance-predictor/
├── data/
├── models/
│   └── student_performance_model.pkl
├── app.py
├── train_model.py
├── prepare_data.py
├── create_dataset.py
├── analyze_data.py
└── README.md
```

## Important Note

The model currently uses a small synthetic dataset created for learning purposes. Its predictions are experimental and should not be used for real academic decisions.

## Outcome

Successfully enhanced the Student Performance AI application with an improved prediction interface, student input validation, and a visual performance indicator.

**Day 17 completed! 🚀**

_365 Days of Building AI – Learning by Building._# Day 17 – Student Performance AI: UI Enhancement

## Overview

On Day 17 of the 365 Days of Building AI challenge, I enhanced the Student Performance AI application by improving its user interface and prediction result presentation.

The application uses a trained Multiple Linear Regression model to estimate a student's final academic score based on multiple performance-related factors.

## Objectives

- Improve the AI prediction interface.
- Add student name input and validation.
- Display predicted scores in a clear format.
- Introduce a visual performance indicator.
- Improve the overall user experience.

## Features Implemented

### 1. Student Information Input

Users can enter:

- Student name
- Daily study hours
- Attendance percentage
- Previous examination score
- Daily sleep hours
- Assignment completion percentage

### 2. Machine Learning Prediction

The application uses the previously trained Multiple Linear Regression model to predict the student's expected final score.

### 3. Improved Prediction Display

- Displays the predicted final score using Streamlit metrics.
- Shows a visual progress bar representing the predicted score percentage.
- Displays a success message after prediction.
- Validates the student name before generating a prediction.

### 4. Dashboard Improvements

- Updated dashboard metrics.
- Improved application description.
- Navigation between Dashboard, Student Analysis, and AI Prediction pages.

## Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Pickle

## Concepts Learned

- Streamlit metrics using `st.metric()`
- Progress indicators using `st.progress()`
- Input validation
- Python's `max()` and `min()` functions
- Improving user experience in ML applications
- Integrating a trained ML model with a Streamlit interface

## Project Structure

```text
student-performance-predictor/
├── data/
├── models/
│   └── student_performance_model.pkl
├── app.py
├── train_model.py
├── prepare_data.py
├── create_dataset.py
├── analyze_data.py
└── README.md
```

## Important Note

The model currently uses a small synthetic dataset created for learning purposes. Its predictions are experimental and should not be used for real academic decisions.

## Outcome

Successfully enhanced the Student Performance AI application with an improved prediction interface, student input validation, and a visual performance indicator.

**Day 17 completed! 🚀**

_365 Days of Building AI – Learning by Building._
