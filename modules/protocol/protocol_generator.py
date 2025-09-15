import streamlit as st

def run_protocol_generator():
    st.subheader("📝 Protocol Generator")
    st.write("Auto-generate protocol sections based on trial phase and therapeutic area.")

    st.selectbox("Trial Phase", ["Phase I", "Phase II", "Phase III"])
    st.text_area("Custom Notes")
    st.button("Generate Protocol PDF")
