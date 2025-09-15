import streamlit as st
from modules.protocol.crf_builder import run_crf_builder
from modules.protocol.protocol_generator import run_protocol_generator
from modules.protocol.sap_generator import run_sap_generator

st.set_page_config(page_title="Protocol & CRF Builder", layout="wide")

st.header("📄 Protocol & CRF Builder")

# CRF + Protocol
run_crf_builder()
run_protocol_generator()

st.header("📊 Statistical Analysis Plan (SAP)")
run_sap_generator()
