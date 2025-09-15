# components/cards.py
import streamlit as st

def render_card(title: str, description: str, key: str, button_label: str = None, on_click=None):
    """
    Render a card with title, description, and optional button.

    Args:
        title (str): The title of the card.
        description (str): Short description text.
        key (str): Unique key for the Streamlit element.
        button_label (str, optional): Label for the button. If None, no button is shown.
        on_click (callable, optional): Function to call when the button is clicked.
    """
    with st.container():
        st.markdown(
            f"""
            <div style="
                border-radius: 12px;
                padding: 1rem;
                margin-bottom: 1rem;
                background-color: #f9f9f9;
                border: 1px solid #ddd;
                box-shadow: 0px 2px 6px rgba(0,0,0,0.05);
            ">
                <h4 style="margin: 0; color: #2C3E50;">{title}</h4>
                <p style="margin-top: 0.5rem; margin-bottom: 0; color: #555;">{description}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if button_label:
            if st.button(button_label, key=key):
                if on_click:
                    on_click()
