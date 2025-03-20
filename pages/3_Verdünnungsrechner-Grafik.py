import streamlit as st

# ====== Start Login Block ======
from utils.login_manager import LoginManager
import pandas as pd
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
import pandas as pd

st.title("📊 Grafik des Verdünnungsrechners")
st.write("Hier sehen Sie die Grafik des Verdünnungsrechners.")

# **Lade gespeicherte Daten aus `session_state`**
data_df = st.session_state.get("data_df", pd.DataFrame())

# **Prüfen, ob Daten vorhanden sind**
if data_df.empty:
    st.info("❌ Keine Verdünnungs-Daten vorhanden. Berechnen Sie Ihre Verdünnung auf der vorherigen Seite.")
    st.stop()

# **🔎 Debugging: Zeige die tatsächlichen Spaltennamen**
st.write("🔎 Verfügbare Spalten:", data_df.columns.tolist())

# **🔹 Sicherstellen, dass `timestamp` als Datetime formatiert ist**
if "timestamp" in data_df.columns:
    data_df["timestamp"] = pd.to_datetime(data_df["timestamp"], errors='coerce')  # Falls fehlerhafte Einträge existieren
    data_df = data_df.dropna(subset=["timestamp"])  # Entferne ungültige Zeilen
    data_df = data_df.set_index("timestamp")  # Setze `timestamp` als Index
else:
    st.error("⚠️ 'timestamp' fehlt in den Daten!")
    st.stop()

# **🔹 Line Charts mit den korrekten Spaltennamen**
st.line_chart(data=data_df["Eingangskonzentration"], use_container_width=True)
st.caption("🔬 Eingangskonzentration (c₁) über Zeit (mol/L)")

st.line_chart(data=data_df["Eingangsvolumen"], use_container_width=True)
st.caption("📦 Eingangsvolumen (V₁) über Zeit (L)")

st.line_chart(data=data_df["Zielkonzentration"], use_container_width=True)
st.caption("🧪 Zielkonzentration (c₂) über Zeit (mol/L)")

st.line_chart(data=data_df["Endvolumen (V2)"], use_container_width=True)
st.caption("📊 Endvolumen (V₂) über Zeit (L)")

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