import streamlit as st
import pandas as pd

def run_patient_screening():
    st.subheader("🏥 Patient Screening Tool")
    st.write("Evaluate inclusion/exclusion criteria.")

    uploaded_file = st.file_uploader("Upload patient CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())
        st.button("Run Eligibility Check")
