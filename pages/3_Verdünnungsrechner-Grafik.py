import streamlit as st

# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======


st.title("Grafik des Verdünnungsrechners")

st.write("Hier sehen Sie die Grafik des Verdünnungsrechners.")

#Grafik
import streamlit as st
import pandas as pd

st.title("Verdünnungsrechner Verlauf")

# Sicherstellen, dass die Daten existieren
if "verduennungs_df" not in st.session_state:
    st.session_state["verduennungs_df"] = pd.DataFrame(columns=["timestamp", "c1", "v1", "c2", "V2"])

data_df = st.session_state["verduennungs_df"]

# Falls keine Daten vorhanden sind
if data_df.empty:
    st.info("Keine gespeicherten Verdünnungsdaten vorhanden. Führen Sie eine Berechnung durch.")
    st.stop()

# Verlauf der Eingangskonzentration (c₁) über die Zeit
st.line_chart(data=data_df.set_index("timestamp")["c1"], use_container_width=True)
st.caption("Eingangskonzentration (c₁) über Zeit (mol/L)")

# Verlauf des Eingangsvolumens (V₁) über die Zeit
st.line_chart(data=data_df.set_index("timestamp")["v1"], use_container_width=True)
st.caption("Eingangsvolumen (V₁) über Zeit (L)")

# Verlauf der Zielkonzentration (c₂) über die Zeit
st.line_chart(data=data_df.set_index("timestamp")["c2"], use_container_width=True)
st.caption("Zielkonzentration (c₂) über Zeit (mol/L)")

# Verlauf des berechneten Endvolumens (V₂) über die Zeit
st.line_chart(data=data_df.set_index("timestamp")["V2"], use_container_width=True)
st.caption("Endvolumen (V₂) über Zeit (L)")

# Optional: Tabelle zur Anzeige der gespeicherten Werte
st.write("Gespeicherte Verdünnungsdaten:")
st.dataframe(data_df)

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