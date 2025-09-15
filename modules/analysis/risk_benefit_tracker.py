import streamlit as st

def run_risk_benefit_tracker():
    st.subheader("⚖️ Risk-Benefit Tracker")
    st.write("Track cumulative risk vs. benefit for enrolled patients.")

    st.checkbox("Show Risk Table")
    st.checkbox("Show Benefit Table")
    st.button("Update Tracker")
