import streamlit as st

def run_crf_builder():
    st.subheader("📄 CRF Builder")
    st.write("Drag-and-drop CRF builder will go here.")

    # Example placeholder form
    st.text_input("Patient ID Field Name", "patient_id")
    st.selectbox("Data Type", ["Text", "Number", "Date"])
    st.button("Add Field")
