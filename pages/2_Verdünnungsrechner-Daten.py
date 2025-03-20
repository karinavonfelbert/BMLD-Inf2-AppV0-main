import streamlit as st

# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======


st.title("Daten des Verdünnungsrechner")

if 'data_df' not in st.session_state or st.session_state['data_df'].empty:
    st.info('Keine Daten vorhanden. Berechnen Sie Ihre Verdünnung im Verdünnungsrechner.')
    st.stop()

data_df = st.session_state['data_df']

data_df = data_df.sort_values('timestamp', ascending=False)

st.dataframe(data_df)


# Hintergrundfarbe

st.markdown(
    """
    <style>
        .stApp, .block-container {
            background: radial-gradient(circle, #C6DE9B, #F9F9F9) !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)


