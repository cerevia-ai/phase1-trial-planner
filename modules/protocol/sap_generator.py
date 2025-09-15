import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.lib.utils import ImageReader
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import io

# -----------------------------
# Helper: Create cohort summary table
# -----------------------------
def create_summary_table(patient_data, columns=["Age", "Weight (kg)", "Height (cm)"]):
    summary = []
    dose_groups = patient_data["Dose Group"].unique()
    for group in dose_groups:
        cohort = patient_data[patient_data["Dose Group"] == group]
        row = [group]
        for col in columns:
            mean = cohort[col].mean()
            std = cohort[col].std()
            row.append(f"{mean:.1f} ± {std:.1f}")
        summary.append(row)
    table_data = [["Dose Group"] + columns] + summary
    return table_data

# -----------------------------
# Helper: Create cohort plots
# -----------------------------
def create_cohort_histograms(patient_data, columns=["Age", "Weight (kg)", "Height (cm)"]):
    images = []
    dose_groups = patient_data["Dose Group"].unique()
    for col in columns:
        plt.figure(figsize=(6,4))
        for group in dose_groups:
            cohort = patient_data[patient_data["Dose Group"] == group]
            plt.hist(cohort[col], alpha=0.5, label=group, bins=8)
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.title(f"{col} Distribution by Cohort")
        plt.legend()
        buf = io.BytesIO()
        plt.savefig(buf, format='PNG')
        plt.close()
        buf.seek(0)
        images.append(buf)
    return images

# -----------------------------
# PDF Generation Logic
# -----------------------------
def generate_sap_pdf(
    trial_title,
    objectives,
    endpoints,
    analysis_populations,
    sample_size,
    dose_groups,
    statistical_methods,
    patient_data=None,
    output_file=None
):
    if output_file is None:
        output_file = f"{trial_title.replace(' ', '_')}_SAP.pdf"

    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter

    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - 50, "Statistical Analysis Plan (SAP)")
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, f"Trial Title: {trial_title}")
    c.drawString(50, height - 120, f"Date: {datetime.now().strftime('%Y-%m-%d')}")

    # Study Objectives
    y = height - 160
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Study Objectives:")
    c.setFont("Helvetica", 12)
    y -= 20
    for obj in objectives:
        c.drawString(70, y, f"- {obj}")
        y -= 20

    # Endpoints
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y - 10, "Endpoints:")
    c.setFont("Helvetica", 12)
    y -= 30
    for ep in endpoints:
        c.drawString(70, y, f"- {ep}")
        y -= 20

    # Dose Groups / Trial Arms
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y - 10, "Trial Arms / Dose Groups:")
    c.setFont("Helvetica", 12)
    y -= 30
    for group in dose_groups:
        c.drawString(70, y, f"- {group}")
        y -= 20

    # Analysis Populations
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y - 10, "Analysis Populations:")
    c.setFont("Helvetica", 12)
    y -= 30
    for pop in analysis_populations:
        c.drawString(70, y, f"- {pop}")
        y -= 20

    # Sample Size Table
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y - 10, "Sample Size by Cohort:")
    y -= 30
    table_data = [["Dose Group", "Planned Patients", "Actual Patients"]]
    actual_counts = {}
    if patient_data is not None:
        df = pd.DataFrame(patient_data)
        actual_counts = df.groupby("Dose Group").size().to_dict()
    for group in dose_groups:
        actual = actual_counts.get(group, 0)
        table_data.append([group, str(sample_size), str(actual)])
    table = Table(table_data, colWidths=[150, 150, 150])
    style = TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightblue),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
    ])
    table.setStyle(style)
    table.wrapOn(c, width, height)
    table.drawOn(c, 50, y - (20 * len(table_data)))
    y -= (20 * (len(table_data)+2))

    # Statistical Methods
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Statistical Methods:")
    c.setFont("Helvetica", 12)
    y -= 20
    for method in statistical_methods:
        c.drawString(70, y, f"- {method}")
        y -= 20

    # -----------------------------
    # Cohort Summary Table & Plots
    # -----------------------------
    if patient_data is not None:
        c.showPage()  # new page for summary & plots
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(width / 2, height - 50, "Patient Demographics Summary")

        # Summary Table
        summary_table_data = create_summary_table(df)
        table = Table(summary_table_data, colWidths=[150, 100, 100, 100])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.lightgreen),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('GRID', (0,0), (-1,-1), 1, colors.black),
        ]))
        table.wrapOn(c, width, height)
        table.drawOn(c, 50, height - 250)

        # Plots
        images = create_cohort_histograms(df)
        img_y = height - 450
        for img_buf in images:
            c.drawImage(ImageReader(img_buf), 50, img_y, width=500, height=200)
            img_y -= 220  # move down for next plot

    c.showPage()
    c.save()
    return output_file

# -----------------------------
# Streamlit Wrapper
# -----------------------------
def run_sap_generator():
    st.subheader("📊 Advanced SAP Generator with Sample Size & Plots")

    trial_title = st.text_input("Trial Title", "Phase I Study of XYZ Drug")

    objectives = st.text_area(
        "Study Objectives (one per line)",
        "Evaluate safety\nAssess PK/PD\nExplore preliminary efficacy"
    ).splitlines()

    endpoints = st.text_area(
        "Endpoints (one per line)",
        "Primary: Safety\nSecondary: PK parameters\nExploratory: Biomarkers"
    ).splitlines()

    if "patients" in st.session_state and st.session_state["patients"]:
        dose_groups = list(set(p["Dose Group"] for p in st.session_state["patients"]))
    else:
        dose_groups = st.text_area(
            "Trial Arms / Dose Groups (one per line)",
            "Cohort 1\nCohort 2\nCohort 3"
        ).splitlines()

    analysis_populations = st.text_area(
        "Analysis Populations (one per line)",
        "ITT\nPer Protocol"
    ).splitlines()

    sample_size = st.number_input("Planned Sample Size per Cohort", min_value=1, value=6, step=1)

    default_methods = [
        "Descriptive statistics for demographics",
        "Safety analysis by dose group",
        "PK/PD summary statistics",
        "Exploratory efficacy analysis"
    ]
    statistical_methods = st.text_area(
        "Statistical Methods (one per line)",
        "\n".join(default_methods)
    ).splitlines()

    if st.button("Generate Advanced SAP PDF"):
        patient_data = st.session_state.get("patients", None)
        pdf_file = generate_sap_pdf(
            trial_title,
            objectives,
            endpoints,
            analysis_populations,
            sample_size,
            dose_groups,
            statistical_methods,
            patient_data=patient_data
        )
        st.success(f"✅ Advanced SAP PDF generated: {pdf_file}")
        st.download_button("⬇ Download SAP PDF", pdf_file, file_name=pdf_file)
