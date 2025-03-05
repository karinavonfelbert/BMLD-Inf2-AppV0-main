import streamlit as st

st.title("Verdünnungsrechner")
st.subheader("Hier finden Sie den Verdünnungsrechner.")

# Eingabe der Konzentrationen und Volumina
c1 = st.number_input("Eingangskonzentration (c1) in mol/L", min_value=0.0, step=0.1)
v1 = st.number_input("Eingangsvolumen (v1) in L", min_value=0.0, step=0.1)
c2 = st.number_input("Zielkonzentration (c2) in mol/L", min_value=0.0, step=0.1)

# Button zur Berechnung
if st.button("Berechnen"):
    if c1 > 0 and v1 > 0 and c2 > 0 and c2 < c1:
        v2 = (c1 * v1) / c2  # Berechnung des Zielvolumens
        st.success(f"Das benötigte Endvolumen (v2) ist: {v2:.3f} L")
    else:
        st.error("Bitte geben Sie gültige Werte ein. c2 muss kleiner als c1 sein.")

import streamlit as st

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