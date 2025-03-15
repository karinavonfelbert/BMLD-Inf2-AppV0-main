import streamlit as st
import pandas as pd
from utils.data_manager import DataManager

st.title("Verdünnungsrechner")
st.markdown("### **Berechnung**")
st.markdown("""
    Die Berechnung basiert auf der Verdünnungsformel:
""")
st.latex(r"c_1 \cdot V_1 = c_2 \cdot V_2")
st.markdown("""
    Wobei das Endvolumen \(V_2\) durch Umstellen der Formel bestimmt wird als:
""")
st.latex(r"V_2 = \frac{c_1 \cdot V_1}{c_2}")
st.markdown("""
    Anschließend wird das benötigte Verdünnungsvolumen berechnet:
""")
st.latex(r"V_D = V_2 - V_1")

st.subheader("Hier finden Sie den Verdünnungsrechner.")

def calculate_dilution(c1, v1, c2):
    if c1 > 0 and v1 > 0 and c2 > 0 and c2 < c1:
        v2 = (c1 * v1) / c2  # Berechnung des Zielvolumens
        return {
            "v2": v2,
            "message": f"Das benötigte Endvolumen (V₂) ist: {v2:.3f} L"
        }
    else:
        return {
            "v2": None,
            "message": "Bitte geben Sie gültige Werte ein. c₂ muss kleiner als c₁ sein."
        }

with st.form("verdünnung_formular"):
    c1 = st.number_input("Eingangskonzentration (c₁) in mol/L", min_value=0.0, step=0.1)
    v1 = st.number_input("Eingangsvolumen (V₁) in L", min_value=0.0, step=0.1)
    c2 = st.number_input("Zielkonzentration (c₂) in mol/L", min_value=0.0, step=0.1)
    berechnen = st.form_submit_button("Berechnen")

if berechnen:
    result = calculate_dilution(c1, v1, c2)
    if result["v2"] is not None:
        st.success(result["message"])
    else:
        st.error(result["message"])
    
    DataManager().append_record(session_state_key='data_df', record_dict=result)

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

df_legende = pd.DataFrame(legende_data)

st.markdown("### **Legende**")
st.table(df_legende)

st.markdown("""
    <style>
        body, .stApp {
            background: radial-gradient(circle, #C6DE9B, #F9F9F9);
        }
        h1, h2, h3, h4, h5, h6, p, div {
            color: black !important;
        }
        input[type="text"], input[type="number"], textarea, select {
            background-color: white !important;
            color: black !important;
            border-radius: 5px !important;
            border: 1px solid black !important;
        }
        button {
            background-color: white !important;
            color: black !important;
            border-radius: 5px !important;
            border: 1px solid black !important;
        }
        .stButton>button {
            background-color: white !important;
            color: black !important;
            border-radius: 5px !important;
            border: 1px solid black !important;
            font-weight: bold !important;
        }
    </style>
""", unsafe_allow_html=True)