# components/forms.py
import streamlit as st

def patient_form():
    """Form for entering patient demographics and baseline data."""
    with st.form("patient_form"):
        st.subheader("Patient Information")
        pid = st.text_input("Patient ID")
        age = st.number_input("Age", min_value=18, max_value=120, step=1)
        sex = st.selectbox("Sex", ["Male", "Female", "Other"])
        weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, step=0.1)
        height = st.number_input("Height (cm)", min_value=100.0, max_value=220.0, step=0.1)
        dose_group = st.selectbox("Dose Group", ["Cohort 1", "Cohort 2", "Cohort 3"])

        submitted = st.form_submit_button("Submit")
        if submitted:
            return {
                "Patient ID": pid,
                "Age": age,
                "Sex": sex,
                "Weight": weight,
                "Height": height,
                "Dose Group": dose_group,
            }
    return None


def adverse_event_form():
    """Form for logging adverse events."""
    with st.form("adverse_event_form"):
        st.subheader("Adverse Event Reporting")
        pid = st.text_input("Patient ID")
        event = st.text_area("Adverse Event Description")
        severity = st.selectbox("Severity", ["Mild", "Moderate", "Severe", "Life-threatening"])
        related = st.selectbox("Related to Study Drug?", ["Yes", "No", "Unknown"])
        outcome = st.selectbox("Outcome", ["Recovered", "Recovering", "Not Recovered", "Fatal", "Unknown"])
        onset_date = st.date_input("Onset Date")
        resolution_date = st.date_input("Resolution Date", value=None)

        submitted = st.form_submit_button("Log Event")
        if submitted:
            return {
                "Patient ID": pid,
                "Event": event,
                "Severity": severity,
                "Related": related,
                "Outcome": outcome,
                "Onset Date": str(onset_date),
                "Resolution Date": str(resolution_date) if resolution_date else None,
            }
    return None


def concomitant_medication_form():
    """Form for recording concomitant medications."""
    with st.form("conmed_form"):
        st.subheader("Concomitant Medication")
        pid = st.text_input("Patient ID")
        med_name = st.text_input("Medication Name")
        indication = st.text_input("Indication")
        dose = st.text_input("Dose (e.g., 50 mg)")
        frequency = st.text_input("Frequency (e.g., once daily)")
        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date", value=None)

        submitted = st.form_submit_button("Record Medication")
        if submitted:
            return {
                "Patient ID": pid,
                "Medication": med_name,
                "Indication": indication,
                "Dose": dose,
                "Frequency": frequency,
                "Start Date": str(start_date),
                "End Date": str(end_date) if end_date else None,
            }
    return None
