import streamlit as st

def sidebar_menu():
    st.sidebar.title("Phase I Trial Assistant")

    menu_options = {
        "Protocol & CRF Builder": "01_protocol",
        "Regulatory & IRB": "02_regulatory",
        "Site Setup & Recruitment": "03_site_management",
        "Data Management & Monitoring": "04_data_management",
        "Analysis: PK/PD & Safety": "05_analysis"
    }

    choice = st.sidebar.radio("Navigate to:", list(menu_options.keys()))
    return menu_options[choice]
