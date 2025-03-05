import streamlit as st
import pandas as pd

st.title("Meine erste Streamlit App")

# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool!
"""
Diese App wurde von folgenden Personen entwickelt:
- Elena Stevanovic (stevaele@students.zhaw.ch)
- Karina von Felbert (vonfekar@students.zhaw.ch)

import streamlit as st

def berechne_verdünnung(c1, v1, c2):
    v2 = (c1 * v1) / c2  # Endvolumen
    v_verdünnungsmittel = v2 - v1  # Menge des Verdünnungsmittels
    return v2, v_verdünnungsmittel

# Streamlit App
st.title("🔬 Verdünnungsrechner für das Labor")
st.write("Berechnet das benötigte Endvolumen und das Volumen des Verdünnungsmittels für eine Lösung.")

# Eingabefelder
c1 = st.number_input("Konzentration der Stammlösung (C1) [z.B. mol/L]", min_value=0.0, format="%.6f")
v1 = st.number_input("Volumen der Stammlösung (V1) [mL]", min_value=0.0, format="%.3f")
c2 = st.number_input("Gewünschte Endkonzentration (C2) [z.B. mol/L]", min_value=0.0, format="%.6f")

if st.button("Berechnen"):
    if c1 > 0 and v1 > 0 and c2 > 0 and c2 < c1:
        v2, v_verdünnungsmittel = berechne_verdünnung(c1, v1, c2)
        st.success(f"Benötigtes Endvolumen: {v2:.3f} mL")
        st.info(f"Benötigtes Volumen des Verdünnungsmittels: {v_verdünnungsmittel:.3f} mL")
    else:
        st.error("Bitte gültige Werte eingeben. C2 muss kleiner als C1 sein.")

