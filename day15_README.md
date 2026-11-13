# Day 15 – Data Preprocessing and Preparation

## Objective

Prepare the Student Performance dataset for machine learning model training by inspecting data quality, separating features and target variables, and splitting the dataset into training and testing sets.

## Project

Student Performance AI – Student Performance Predictor

## Tools and Libraries

- Python
- Pandas
- Scikit-learn

## Tasks Completed

### 1. Dataset Loading

- Loaded the student dataset using Pandas.
- Inspected the first five records.
- Checked the dataset dimensions.

### 2. Feature and Target Separation

Separated the dataset into:

**Input Features (X):**

- study_hours
- attendance
- previous_score
- sleep_hours
- assignment_completion

**Target Variable (y):**

- final_score

### 3. Data Quality Checks

- Checked missing values using `df.isnull().sum()`.
- Checked duplicate records using `df.duplicated().sum()`.
- Found zero missing values and zero duplicate records.

### 4. Training and Testing Split

Used Scikit-learn's `train_test_split()`.

Configuration:

- Training data: 80% (16 records)
- Testing data: 20% (4 records)
- Random state: 42

### 5. Saving Prepared Data

Saved the prepared datasets as separate CSV files:

- X_train.csv
- X_test.csv
- y_train.csv
- y_test.csv

## Concepts Learned

- Data preprocessing
- Features and target variables
- Input-output separation
- Missing value detection
- Duplicate detection
- Training and testing datasets
- Train-test splitting
- Reproducibility using random_state

## Key Learning

Data preprocessing is an important step in machine learning. It helps organize and prepare raw data before training a model.

Training data is used to teach the model, while testing data is used to evaluate its performance on unseen records.

## Dataset Information

- Total records: 20
- Total columns: 6
- Input features: 5
- Target variable: 1
- Missing values: 0
- Duplicate records: 0

**Note:** This project uses a small synthetic dataset for educational purposes.

## Outcome

Successfully completed the initial data preprocessing workflow and prepared the dataset for machine learning model training.

**Day 15 of 365 Days of Building AI – Completed!**
