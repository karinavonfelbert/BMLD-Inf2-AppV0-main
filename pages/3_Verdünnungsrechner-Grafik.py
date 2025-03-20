import streamlit as st

# ====== Start Login Block ======
from utils.login_manager import LoginManager
import pandas as pd
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======


st.title("Grafik des Verdünnungsrechners")

st.write("Hier sehen Sie die Grafik des Verdünnungsrechners.")

# Load data from session state
import pandas as pd
import streamlit as st

data_df = st.session_state.get('data_df', pd.DataFrame())

if data_df.empty:
    st.info('Keine Verdünnungsrechner-Daten vorhanden. Bitte geben Sie Ihre Daten auf der vorherigen Seite ein.')
    st.stop()

# Plot concentration over time
st.line_chart(data=data_df.set_index('timestamp')['concentration'], 
              use_container_width=True)
st.caption('Konzentration über Zeit')

# Plot volume over time
st.line_chart(data=data_df.set_index('timestamp')['volume'],
              use_container_width=True)
st.caption('Volumen über Zeit')

# Plot dilution factor over time
st.line_chart(data=data_df.set_index('timestamp')['dilution_factor'],
              use_container_width=True)
st.caption('Verdünnungsfaktor über Zeit')



# Hintergrundfarbe

st.markdown(
    """
    <style>
        body, .stApp {
            background: radial-gradient(circle, #C6DE9B, #F9F9F9) !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Schriftfarbe

st.markdown("""
    <style>
        h1, h2, h3, h4, h5, h6, p, div {
            color: black !important;
        }
    </style>
    """, unsafe_allow_html=True)