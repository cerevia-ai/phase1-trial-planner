import streamlit as st

def run_submission_packager():
    st.subheader("📑 Regulatory Submission Packager")
    st.write("Automatically create IND/IRB submission packages.")

    st.file_uploader("Upload protocol and CRFs")
    st.button("Generate Submission PDF")
