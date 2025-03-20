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


st.title("Verdünnungsrechner")

# Sicherstellen, dass der Session State für die Speicherung existiert
if "verduennungs_df" not in st.session_state:
    st.session_state["verduennungs_df"] = pd.DataFrame(columns=["timestamp", "c1", "v1", "c2", "V2"])

# Eingabefelder für die Verdünnung
c1 = st.number_input("Eingangskonzentration (c₁) in mol/L", min_value=0.0, step=0.1)
v1 = st.number_input("Eingangsvolumen (V₁) in L", min_value=0.0, step=0.1)
c2 = st.number_input("Zielkonzentration (c₂) in mol/L", min_value=0.0, step=0.1)

# Funktion zur Berechnung des Verdünnungsvolumens
def berechne_verduennung(c1, v1, c2):
    if c1 > 0 and v1 > 0 and c2 > 0 and c2 < c1:
        v2 = (c1 * v1) / c2
        return v2
    else:
        return None

# Berechnung starten
if st.button("Berechnen"):
    v2 = berechne_verduennung(c1, v1, c2)
    if v2 is not None:
        st.success(f"Das benötigte Endvolumen (V₂) ist: {v2:.3f} L")
        
        # **Neue Berechnung in die Session-Daten speichern**
        new_data = pd.DataFrame([{"timestamp": pd.Timestamp.now(), "c1": c1, "v1": v1, "c2": c2, "V2": v2}])
        st.session_state["verduennungs_df"] = pd.concat([st.session_state["verduennungs_df"], new_data], ignore_index=True)
    else:
        st.error("Bitte geben Sie gültige Werte ein. c₂ muss kleiner als c₁ sein.")

# **Verlinkung zur Verlaufsseite**
st.page_link("verlauf.py", label="Zum Verlauf der Verdünnungswerte 📈")


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