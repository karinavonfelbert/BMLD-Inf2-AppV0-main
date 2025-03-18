import streamlit as st
from utils import helpers  # Hier den Pfad zu deiner helpers.py anpassen

# Funktion zur Berechnung des Verdünnungsvolumens (Basierend auf den Daten aus deinem Screenshot)
def calculate_dilution(c1, v1, c2):
    """
    Berechnet das Zielvolumen (V2) und das Verdünnungsvolumen (V_D).
    """
    if c1 > 0 and v1 > 0 and c2 > 0 and c2 < c1:
        v2 = (c1 * v1) / c2  # Berechnung des Zielvolumens
        v_d = v2 - v1  # Berechnung des Verdünnungsvolumens
        return {
            "v2": v2,
            "v_d": v_d,
            "message": f"Das benötigte Endvolumen (V2) ist: {v2:.3f} L. Das Verdünnungsvolumen (V_D) ist: {v_d:.3f} L"
        }
    else:
        return {
            "v2": None,
            "v_d": None,
            "message": "Bitte geben Sie gültige Werte ein. c2 muss kleiner als c1 sein und alle Werte müssen größer als 0 sein."
        }

# Streamlit Interface
st.title("Verdünnungsrechner")
st.markdown("### **Berechnung der Verdünnung**")

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

with st.form("verdünnung_formular"):
    c1 = st.number_input("Eingangskonzentration (c1) in mol/L", min_value=0.0, step=0.1)
    v1 = st.number_input("Eingangsvolumen (V1) in L", min_value=0.0, step=0.1)
    c2 = st.number_input("Zielkonzentration (c2) in mol/L", min_value=0.0, step=0.1)
    
    submitted = st.form_submit_button("Berechnen")

if submitted:
    result = calculate_dilution(c1, v1, c2)
    if result["v2"] is not None:
        # Erfolgreiche Berechnung - Speichern der Daten
        record_dict = {
            "timestamp": helpers.ch_now(),  # Stelle sicher, dass helpers.ch_now() die richtige Funktion ist, um die aktuelle Zeit zu holen
            "c1": c1,
            "v1": v1,
            "c2": c2,
            "v2": result["v2"],
            "v_d": result["v_d"],
            "message": result["message"]
        }
        
        # Speicherung der Ergebnisse in Session State (oder auf SwitchDrive hochladen)
        if 'data_df' not in st.session_state:
            st.session_state['data_df'] = []
        
        st.session_state['data_df'].append(record_dict)

        # Daten anzeigen
        st.success(result["message"])
    else:
        st.error(result["message"])
