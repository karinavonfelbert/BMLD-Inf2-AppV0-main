import streamlit as st
import pandas as pd

st.title("Meine erste Streamlit App")

# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool!
"""
Diese App wurde von folgenden Personen entwickelt:
- Elena Stevanovic (stevaele@students.zhaw.ch)
- Karina von Felbert (vonfekar@students.zhaw.ch)
"""

Präzise Verdünnungen für exakte Laborergebnisse
Dieser Verdünnungsrechner hilft Ihnen, schnell und zuverlässig die benötigten Volumina für Ihre Lösungen zu berechnen. Vermeiden Sie Rechenfehler und stellen Sie sicher, dass Ihre Verdünnungen stets den gewünschten Konzentrationen entsprechen.


import streamlit as st

# Sidebar für Navigation
st.sidebar.title("Navigation")
seite = st.sidebar.radio("Wähle eine Seite", ["Start", "Unterseite A", "Unterseite B"])

# Inhalte der Seiten
if seite == "Start":
    st.title("Willkommen auf der Startseite")
    st.write("Dies ist die Hauptseite.")

elif seite == "Unterseite A":
    st.title("Unterseite A - Verdünnungsrechner")
    st.write("Hier kannst du deine Verdünnung berechnen.")

    # 📌 Hier kommt dein Code für den Verdünnungsrechner rein:
    def berechne_verdünnung(c1, v1, c2):
        v2 = (c1 * v1) / c2  # Endvolumen
        v_verdünnungsmittel = v2 - v1  # Menge des Verdünnungsmittels
        return v2, v_verdünnungsmittel

    # Eingabefelder
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
    st.write("Hier könnte ein anderer Rechner oder eine andere Funktion sein.")
