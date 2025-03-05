import streamlit as st
import pandas as pd

st.title("Verdünnungsrechner")

# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

st.write(
    """
    Der Verdünnungsrechner ist eine benutzerfreundliche Webanwendung, die entwickelt wurde, um Laborpersonal, Studierenden und Forschenden bei der Berechnung von Verdünnungen zu unterstützen. Mithilfe dieser App können Benutzer schnell das benötigte Volumen einer Stamm- oder Endlösung berechnen, um eine gewünschte Verdünnung zu erhalten.
    """
)
"""
Diese App wurde von folgenden Personen entwickelt:
- Elena Stevanovic (stevaele@students.zhaw.ch)
- Karina von Felbert (vonfekar@students.zhaw.ch)
"""
import streamlit as st

import streamlit as st

st.markdown(
    """
    <style>
        body, .stApp {
            background: linear-gradient(to bottom, #C6DE9B, #F9F9F9); 
        }
    </style>
    """,
    unsafe_allow_html=True
)

[theme]
textColor = "#000000"  # Schwarz
