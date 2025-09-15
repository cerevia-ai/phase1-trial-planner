import streamlit as st

def run_pkpd_simulator():
    st.subheader("💉 PK/PD Simulator")
    st.write("Simulate pharmacokinetics/pharmacodynamics scenarios.")

    st.number_input("Starting Dose (mg)", min_value=0.1, max_value=100.0, value=10.0)
    st.slider("Number of Patients", min_value=1, max_value=50, value=10)
    st.button("Run Simulation")
