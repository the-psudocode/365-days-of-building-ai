
import streamlit as st
import pickle
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Student Performance AI",
    page_icon="🎓",
    layout="wide"
)

# Load the trained machine learning model
with open("models/student_performance_model.pkl", "rb") as file:
    model = pickle.load(file)

# Custom CSS
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


# Sidebar navigation
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
    st.info("Project 01 | Day 16 of 365")


# Page navigation
page = st.session_state.get("page", "Dashboard")


# Student Analysis Page
if page == "Student Analysis":

    st.title("📊 Student Analysis")
    st.info("Student analysis features will be developed here.")


# AI Prediction Page
elif page == "AI Prediction":

    st.title("🤖 AI Student Performance Prediction")

    st.write(
        "Enter student details below to predict their expected final score."
    )

    st.divider()

    st.subheader("Student Information")

    col1, col2 = st.columns(2)

    with col1:

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

    # Prediction button
    if st.button(
        "🔮 Predict Student Performance",
        use_container_width=True
    ):

        # Prepare student input
        student_data = pd.DataFrame([{
            "study_hours": study_hours,
            "attendance": attendance,
            "previous_score": previous_score,
            "sleep_hours": sleep_hours,
            "assignment_completion": assignment_completion
        }])

        # Generate prediction
        prediction = model.predict(student_data)

        # Display result
        st.success("Prediction completed successfully!")

        st.metric(
            "Predicted Final Score",
            f"{prediction[0]:.2f} / 100"
        )


# Dashboard Page
else:

    st.markdown(
        '<div class="main-title">Student Performance Dashboard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Analyze academic information and predict student performance using Machine Learning.</div>',
        unsafe_allow_html=True
    )
