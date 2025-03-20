import streamlit as st

# ====== Start Login Block ======
from utils.login_manager import LoginManager
import pandas as pd
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
st.title("Grafik des Verdünnungsrechners")
st.write("Hier sehen Sie die Grafik des Verdünnungsrechners.")

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Verdünnungs-Daten vorhanden. Berechnen Sie Ihre Verdünnung auf der Startseite.')
    st.stop()
    
st.write("🔎 Verfügbare Spalten:", data_df.columns.tolist())

# Falls eine Spalte fehlt, Fehler anzeigen
required_columns = ["timestamp", "c1", "v1", "c2", "V2"]
missing_columns = [col for col in required_columns if col not in data_df.columns]

if missing_columns:
    st.error(f"⚠️ Fehlende Spalten: {', '.join(missing_columns)}")
    st.stop()

# Daten nach Zeitachse indexieren
data_df["timestamp"] = pd.to_datetime(data_df["timestamp"])  # Falls nötig
data_df = data_df.set_index("timestamp")


st.line_chart(data=data_df.set_index('timestamp')['c1'], 
                use_container_width=True)
st.caption('Eingangskonzentration (c₁) über Zeit (mol/L)')

st.line_chart(data=data_df.set_index('timestamp')['mol/L'],
                use_container_width=True)
st.caption('Eingangsvolumen (V₁) über Zeit (L)')

st.line_chart(data=data_df.set_index('timestamp')['v1'],
                use_container_width=True)
st.caption('Zielkonzentration (c₂) über Zeit (mol/L)')

st.line_chart(data=data_df.set_index('timestamp')['c2'],
                use_container_width=True)
st.line_chart(data=data_df.set_index('timestamp')['V2'],
                use_container_width=True)

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