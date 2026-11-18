
import streamlit as st
import pickle
import pandas as pd

# ----------------------------------
# 1. Page Configuration
# ----------------------------------

st.set_page_config(
    page_title="Student Performance AI",
    page_icon="🎓",
    layout="wide"
)

# ----------------------------------
# 2. Load Machine Learning Model
# ----------------------------------

with open("models/student_performance_model.pkl", "rb") as file:
    model = pickle.load(file)

# ----------------------------------
# 3. Custom CSS
# ----------------------------------

st.markdown("""
<style>
    .stApp {
        background-color: #F4F7FB;
    }

    .main-title {
        font-size: 34px;
        font-weight: 750;
        color: #172554;
    }

    .subtitle {
        color: #64748B;
        font-size: 21px;
        font-weight: 650;
    }

    div[data-testid="stMetric"] {
        background: white;
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------------
# 4. Sidebar Navigation
# ----------------------------------

with st.sidebar:

    st.title("🎓 Student AI")
    st.caption("Academic Intelligence Platform")

    st.divider()

    st.markdown("### Navigation")

    if st.button("🏠 Dashboard", use_container_width=True):
        st.session_state.page = "Dashboard"

    if st.button("📊 Student Analysis", use_container_width=True):
        st.session_state.page = "Student Analysis"

    if st.button("🤖 AI Prediction", use_container_width=True):
        st.session_state.page = "AI Prediction"

    st.divider()

    st.info("Project 01 | Day 17 of 365")


# ----------------------------------
# 5. Page Navigation
# ----------------------------------

page = st.session_state.get("page", "Dashboard")


# ----------------------------------
# 6. Student Analysis Page
# ----------------------------------

if page == "Student Analysis":

    st.title("📊 Student Analysis")

    st.info(
        "Student analysis features will be developed here."
    )


# ----------------------------------
# 7. AI Prediction Page
# ----------------------------------

elif page == "AI Prediction":

    st.title("🤖 AI Student Performance Prediction")

    st.write(
        "Enter student details below to predict their expected final score."
    )

    st.divider()

    st.subheader("Student Information")

    # Input fields
    col1, col2 = st.columns(2)

    with col1:

        student_name = st.text_input(
            "Student Name",
            placeholder="Enter student name"
        )

        study_hours = st.number_input(
            "Daily Study Hours",
            min_value=0.0,
            max_value=24.0,
            value=4.0
        )

        attendance = st.number_input(
            "Attendance (%)",
            min_value=0.0,
            max_value=100.0,
            value=75.0
        )

        previous_score = st.number_input(
            "Previous Exam Score",
            min_value=0.0,
            max_value=100.0,
            value=60.0
        )

    with col2:

        sleep_hours = st.number_input(
            "Daily Sleep Hours",
            min_value=0.0,
            max_value=24.0,
            value=7.0
        )

        assignment_completion = st.number_input(
            "Assignment Completion (%)",
            min_value=0.0,
            max_value=100.0,
            value=80.0
        )

    st.divider()

    # ----------------------------------
    # 8. Prediction
    # ----------------------------------

    if st.button(
        "🔮 Predict Student Performance",
        use_container_width=True
    ):

        if not student_name.strip():

            st.warning("Please enter the student's name.")

        else:

            # Prepare input data
            student_data = pd.DataFrame([{
                "study_hours": study_hours,
                "attendance": attendance,
                "previous_score": previous_score,
                "sleep_hours": sleep_hours,
                "assignment_completion": assignment_completion
            }])

            # Generate prediction
            prediction = model.predict(student_data)

            predicted_score = float(prediction[0])

            # Keep displayed score within 0–100
            score_percentage = max(
                0.0,
                min(100.0, predicted_score)
            )

            # Display result
            st.success("Prediction completed successfully!")

            st.subheader("Prediction Result")

            st.write(f"Student: **{student_name}**")

            st.metric(
                "Predicted Final Score",
                f"{predicted_score:.2f} / 100"
            )

            # Visual performance indicator
            st.subheader("Performance Indicator")

            st.progress(score_percentage / 100)

            st.write(
                f"Predicted score: {score_percentage:.2f}%"
            )

            st.caption(
                "This is a model-based estimate, not a guaranteed exam result."
            )


# ----------------------------------
# 9. Dashboard Page
# ----------------------------------

else:

    st.markdown(
        '<div class="main-title">Student Performance Dashboard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Analyze academic information and predict student performance using Machine Learning.</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.subheader("Welcome to Student Performance AI 🎓")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "AI Model",
            "Connected"
        )

    with col2:
        st.metric(
            "Prediction System",
            "Ready"
        )

    with col3:
        st.metric(
            "Project Progress",
            "Day 17"
        )

    st.divider()

    st.info(
        "Navigate to AI Prediction to estimate a student's final score."
    )

    st.markdown(
        """
        ### About this application

        Student Performance AI uses Machine Learning to estimate
        student academic performance based on:

        - Daily study hours
        - Attendance percentage
        - Previous examination score
        - Daily sleep hours
        - Assignment completion percentage

        **Machine Learning Algorithm:** Multiple Linear Regression
        """
    )
