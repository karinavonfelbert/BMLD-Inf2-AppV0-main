import streamlit as st
import pandas as pd

from utils.data_manager import DataManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD_App_DB")  # switch drive 

# load the data from the persistent storage into the session state
data_manager.load_app_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )

st.title("Verdünnungsrechner")

# !! WICHTIG: Eure Emails müssen in der App erscheinen!!
# CSS für die grüne Info-Box
st.markdown(
    """
    <style>
    .infobox {
        background-color: #96CC6C;  /* Hintergrund: Hellgrün */
        color: black;  /* Schwarzer Text */
        padding: 15px;  /* Innenabstand für mehr Platz */
        border-radius: 10px;  /* Abgerundete Ecken */
        font-size: 16px;  /* Schriftgröße */
        border: 2px solid #5dc95b;  /* Etwas dunklerer grüner Rand */
    }
    </style>
    """,
    unsafe_allow_html=True  
)

st.markdown(
    """
    <div class="infobox">
        Der Verdünnungsrechner ist eine benutzerfreundliche Webanwendung, die entwickelt wurde, um
        Laborpersonal, Studierenden und Forschenden bei der Berechnung von Verdünnungen zu unterstützen.
        Mithilfe dieser App können Benutzer schnell das benötigte Volumen einer Stamm- oder Endlösung berechnen,
        um eine gewünschte Verdünnung zu erhalten.
    </div>
    """,
    unsafe_allow_html=True  
)

st.markdown(
    """
    <style>
    body, .stApp {  /* ✅ Leerzeichen nach Komma hinzugefügt */
        background: radial-gradient(circle, #C6DE9B, #F9F9F9);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    h1, h2, h3, h4, h5, h6, p, div {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
"""
Diese App wurde von folgenden Personen entwickelt:
- Elena Stevanovic (stevaele@students.zhaw.ch)
- Karina von Felbert (vonfekar@students.zhaw.ch)
"""
