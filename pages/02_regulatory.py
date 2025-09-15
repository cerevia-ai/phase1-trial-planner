import streamlit as st
from modules.regulatory.submission_packager import run_submission_packager

st.set_page_config(page_title="Regulatory & IRB", layout="wide")

st.header("📝 Regulatory & IRB")

run_submission_packager()
