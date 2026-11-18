# Day 18 – Student Performance AI: Prediction History

## Overview

On Day 18 of the 365 Days of Building AI challenge, I implemented a prediction history feature in the Student Performance AI application.

The application can now store multiple student predictions during an active session and display them in an interactive table.

## Objectives

- Store multiple student predictions.
- Maintain student information and prediction results.
- Record prediction date and time.
- Display prediction history.
- Provide an option to clear saved history.

## Features Implemented

### 1. Session-Based Storage

Used Streamlit's `st.session_state` to maintain prediction records across application reruns.

### 2. Prediction Records

Each record stores:

- Student name
- Study hours
- Attendance
- Previous examination score
- Sleep hours
- Assignment completion
- Predicted final score
- Prediction date and time

### 3. Prediction History Dashboard

- Displays saved predictions in an interactive table.
- Shows the total number of predictions.
- Provides an empty-state message when no records exist.

### 4. Clear History

Implemented a button to clear all saved prediction records.

## Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Datetime

## Concepts Learned

- Streamlit session state
- Python dictionaries and lists
- Appending records using `.append()`
- Converting dictionaries into Pandas DataFrames
- Displaying interactive tables using `st.dataframe()`
- Working with date and time
- Refreshing Streamlit applications using `st.rerun()`

## Important Note

Prediction history currently uses session-based storage. Records are temporary and are not permanently stored in a database.

Persistent storage using SQLite will be explored in a later development stage.

## Outcome

Successfully implemented a prediction history system that allows users to save, view, count, and clear student prediction records.

**Day 18 completed! 🚀**

_365 Days of Building AI – Learning by Building._
