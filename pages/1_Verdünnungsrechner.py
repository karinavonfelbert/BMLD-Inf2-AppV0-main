# ====== Start Login Block ======
from utils.login_manager import LoginManager
from utils.data_manager import DataManager
from utils.helpers import ch_now
LoginManager().go_to_login('Start.py') 

# ====== End Login Block ======

# ------------------------------------------------------------
# Here starts the actual app, which was developed previously

import streamlit as st

# Titel der App
st.title('Verdünnungsrechner')

# Eingabefelder für die Berechnung
c1 = st.number_input("Eingangskonzentration (c₁) in mol/L", min_value=0.0, step=0.1)
v1 = st.number_input("Eingangsvolumen (V₁) in L", min_value=0.0, step=0.1)
c2 = st.number_input("Zielkonzentration (c₂) in mol/L", min_value=0.0, step=0.1)

# Funktion zur Berechnung des Verdünnungsvolumens
def berechne_verdünnung(c1, v1, c2):
    if c1 > 0 and v1 > 0 and c2 > 0 and c2 < c1:
        v2 = (c1 * v1) / c2
        return {
            "V2": v2,
            "message": f"Das benötigte Endvolumen (V₂) ist: {v2:.3f} L"
        }
    else:
        return {
            "V2": None,
            "message": "Bitte geben Sie gültige Werte ein. c₂ muss kleiner als c₁ sein."
        }

result = None  # Initialisierung, damit es außerhalb des Buttons-Scopes existiert

if st.button("Berechnen"):
    result = berechne_verdünnung(c1, v1, c2)
    
    if result and "V2" in result:
        result_dict = {
            'timestamp': ch_now(),
            'Eingangskonzentration': c1,
            'Eingangsvolumen': v1,
            'Zielkonzentration': c2,
            'Endvolumen (V2)': result["V2"]
        }
        DataManager().append_record(session_state_key='data_df', record_dict=result_dict)
        st.dataframe(st.session_state['data_df'], width=500, height=200)

import pandas as pd

legende_data = {
    "Symbol": ["c₁", "V₁", "c₂", "V₂", "Vd"],
    "Bedeutung": [
        "Eingangskonzentration (mol/L) – Konzentration der Stammlösung vor der Verdünnung",
        "Eingangsvolumen (L) – Volumen der Stammlösung",
        "Zielkonzentration (mol/L) – Gewünschte Endkonzentration nach der Verdünnung",
        "Endvolumen (L) – Endvolumen der Lösung nach der Verdünnung",
        "Verdünnungsmittelvolumen (L) – Benötigte Menge des Verdünnungsmittels (V₂ - V₁)"
    ]
}

# Legende als Dataframe
df_legende = pd.DataFrame(legende_data)

st.markdown("### **Legende**")

st.markdown(
    """
    <style>
    table {
        background-color: white !important; /* Weißer Hintergrund */
        color: black !important; /* Schwarze Schrift */
        font-size: 16px !important; /* Schriftgröße */
        border-collapse: collapse !important; /* Ränder zusammenführen */
        width: 100% !important; /* Maximale Breite */
    }
    th, td {
        border: 2px solid black !important; /* Schwarze Ränder */
        padding: 10px !important; /* Abstand */
        text-align: left !important; /* Text linksbündig */
    }
    th {
        background-color: white !important; /* Hintergrund weiß für Kopfzeile */
        color: black !important; /* Schwarze Schrift für Kopfzeile */
        font-weight: bold !important; /* Fettschrift für Kopfzeile */
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Hintergrundfarbe

st.table(df_legende)

st.markdown(
    """
    <style>
        body, .stApp {
            background: radial-gradient(circle, #C6DE9B, #F9F9F9);
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <style>
        h1, h2, h3, h4, h5, h6, p, div {
            color: black !important;
        }
    </style>
    """, unsafe_allow_html=True)


st.markdown("""
    <style>
    /* Hintergrundfarbe der Eingabefelder */
    input[type="text"], input[type="number"], textarea, select {
        background-color: white !important;
        color: black !important;
        border-radius: 5px !important;
        border: 1px solid black !important;
    }

    /* Hintergrundfarbe und Textfarbe des Buttons */
    button {
        background-color: white !important;
        color: black !important;
        border-radius: 5px !important;
        border: 1px solid black !important;
    }

    /* Spezifisch für Streamlit-Buttons */
    .stButton>button {
        background-color: white !important;
        color: black !important;
        border-radius: 5px !important;
        border: 1px solid black !important;
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)


