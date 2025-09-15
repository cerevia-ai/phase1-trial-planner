import streamlit as st
from modules.analysis.pkpd_simulator import run_pkpd_simulator
from modules.analysis.safety_dashboard import run_safety_dashboard
from modules.analysis.dose_escalation import run_dose_escalation
from modules.analysis.risk_benefit_tracker import run_risk_benefit_tracker

st.set_page_config(page_title="Analysis: PK/PD & Safety", layout="wide")

st.header("💉 Analysis: PK/PD & Safety")

run_pkpd_simulator()
run_safety_dashboard()
run_dose_escalation()
run_risk_benefit_tracker()
