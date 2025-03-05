import streamlit as st
import pandas as pd

st.title("Verdünnungsrechner")

# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

st.write(
    """
    **Der Verdünnungsrechner ist eine benutzerfreundliche Webanwendung, die entwickelt wurde, um Laborpersonal, Studierenden und Forschenden bei der Berechnung von Verdünnungen zu unterstützen. Mithilfe dieser App können Benutzer schnell das benötigte Volumen einer Stamm- oder Endlösung berechnen, um eine gewünschte Verdünnung zu erhalten.
    """
)
"""
Diese App wurde von folgenden Personen entwickelt:
- Elena Stevanovic (stevaele@students.zhaw.ch)
- Karina von Felbert (vonfekar@students.zhaw.ch)
"""





import streamlit as st

import streamlit as st

# Navigation nur in der Sidebar
st.sidebar.title("Navigation")
seite = st.sidebar.radio("Wähle eine Seite", ["Start", "Unterseite A", "Unterseite B"])

# Inhalte der Seiten
if seite == "Start":

elif seite == "Unterseite A":
    st.title("Verdünnungsrechner")
    st.write("Hier kannst du deine Verdünnung berechnen.")

    # 📌 Verdünnungsrechner-Code
    def berechne_verdünnung(c1, v1, c2):
        v2 = (c1 * v1) / c2  # Endvolumen
        v_verdünnungsmittel = v2 - v1  # Menge des Verdünnungsmittels
        return v2, v_verdünnungsmittel

    # Eingabefelder für den Rechner
    c1 = st.number_input("Konzentration der Stammlösung (C1) [mol/L]", min_value=0.0, format="%.6f")
    v1 = st.number_input("Volumen der Stammlösung (V1) [mL]", min_value=0.0, format="%.3f")
    c2 = st.number_input("Gewünschte Endkonzentration (C2) [mol/L]", min_value=0.0, format="%.6f")

    if st.button("Berechnen"):
        if c1 > 0 and v1 > 0 and c2 > 0 and c2 < c1:
            v2, v_verdünnungsmittel = berechne_verdünnung(c1, v1, c2)
            st.success(f"Benötigtes Endvolumen: {v2:.3f} mL")
            st.info(f"Benötigtes Volumen des Verdünnungsmittels: {v_verdünnungsmittel:.3f} mL")
        else:
            st.error("Bitte gültige Werte eingeben. C2 muss kleiner als C1 sein.")

elif seite == "Unterseite B":
    st.title("Unterseite B")
    st.write("Hier könnte eine andere Berechnung oder ein weiteres Tool stehen.")
