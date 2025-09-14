import streamlit as st

st.set_page_config(
    page_title="Phase I Trial Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🧪 Phase I Trial Assistant")
st.markdown(
    """
    Welcome to the **Phase I Trial Assistant**.
    Use the sidebar to navigate through the workflow:
    - 📄 Protocol & CRF Builder
    - 📝 Regulatory & IRB
    - 🏥 Site Management
    - 📊 Data Management
    - 💉 Analysis: PK/PD & Safety
    """
)
