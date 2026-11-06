import streamlit as st

st.set_page_config(
  page_title = "Student Performance AI",
  page_icon = "🎓",
  layout = "wide"
)

st.markdown("""
<style>
  .stApp{
    background-color: #F4F7FB;
    }
    
    .main-title{
      font-size: 34px;
      font-weight: 750;
      color: #172554
    }

    .subtitle{
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
""", unsafe_allow_html = True)

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

  st.info("Project 01 | Day 12 of 365")

# Page navigation
page = st.session_state.get("page", "Dashboard")

if page == "Student Analysis":
    st.title("📊 Student Analysis")
    st.info("Student analysis features will be developed here.")
    st.stop()

elif page == "AI Prediction":
    st.title("🤖 AI Prediction")
    st.info("The trained machine learning model will be connected here.")
    st.stop()

st.markdown(
    '<div class="main-title">Student Performance Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Analyze academic information and predict student performance using Machine Learning.</div>',
    unsafe_allow_html=True
)