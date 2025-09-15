import streamlit as st

def run_safety_dashboard():
    st.subheader("⚠️ Safety Signal Dashboard")
    st.write("Monitor adverse events and safety trends in real-time.")

    st.checkbox("Show AE Summary Table")
    st.checkbox("Show Lab Trends")
    st.button("Refresh Dashboard")
