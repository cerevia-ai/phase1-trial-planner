# components/tables.py
import streamlit as st
import pandas as pd


def render_patient_table():
    """Display patient demographics and baseline data."""
    st.subheader("Patient Registry")
    patients = st.session_state.get("patients", [])
    if patients:
        df = pd.DataFrame(patients)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No patient data available.")


def render_adverse_event_table():
    """Display logged adverse events."""
    st.subheader("Adverse Events")
    events = st.session_state.get("adverse_events", [])
    if events:
        df = pd.DataFrame(events)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No adverse events logged yet.")


def render_conmed_table():
    """Display recorded concomitant medications."""
    st.subheader("Concomitant Medications")
    meds = st.session_state.get("conmeds", [])
    if meds:
        df = pd.DataFrame(meds)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No concomitant medications recorded.")


def render_all_tables():
    """
    Convenience function to render all clinical data tables.
    Can be called from within a page function in app.py.
    """
    render_patient_table()
    render_adverse_event_table()
    render_conmed_table()
