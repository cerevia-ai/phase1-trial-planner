import streamlit as st
from components.forms import patient_form, adverse_event_form, concomitant_medication_form
from components.tables import render_all_tables
from modules.site_management.patient_screening import run_patient_screening

st.set_page_config(page_title="Site Management", layout="wide")

st.header("🏥 Site Setup & Recruitment")

# Patient Screening Module
run_patient_screening()

st.divider()
st.subheader("Clinical Data Entry")

# Forms
patient_data = patient_form()
if patient_data:
    st.session_state.setdefault("patients", []).append(patient_data)

ae_data = adverse_event_form()
if ae_data:
    st.session_state.setdefault("adverse_events", []).append(ae_data)

conmed_data = concomitant_medication_form()
if conmed_data:
    st.session_state.setdefault("conmeds", []).append(conmed_data)

# Tables
st.divider()
render_all_tables()
