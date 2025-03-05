import streamlit as st

st.title("1_Verdünnungsrechner")

st.write("Hier finden Sie den Verdünnungsrechner.")

# Eingabe der Konzentrationen und Volumina
c1 = st.number_input("Eingangskonzentration (c1) in mol/L", min_value=0.0, step=0.1)
v1 = st.number_input("Eingangsvolumen (v1) in L", min_value=0.0, step=0.1)
c2 = st.number_input("Zielkonzentration (c2) in mol/L", min_value=0.0, step=0.1)

# Berechnung des Zielvolumens
if c1 > 0 and c2 > 0:
    v2 = (c1 * v1) / c2
    st.write(f"Das benötigte Endvolumen (v2) ist: {v2} L")
else:
    st.write("Bitte geben Sie gültige Werte für c1 und c2 ein.")