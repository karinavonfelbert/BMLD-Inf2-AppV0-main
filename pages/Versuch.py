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

# Berechnung ausführen
if st.button("Berechnen"):
    result = berechne_verdünnung(c1, v1, c2)

    if result["V2"] is not None:
        result_dict = {
            'timestamp': ch_now(),
            'Eingangskonzentration': c1,
            'Eingangsvolumen': v1,
            'Zielkonzentration': c2,
            'Endvolumen (V2)': result["V2"]
        }
        DataManager().append_record(session_state_key='data_df', record_dict=result_dict)
        st.dataframe(st.session_state['data_df'], width=500, height=200)

        st.success(result["message"])
    else:
        st.error(result["message"])

