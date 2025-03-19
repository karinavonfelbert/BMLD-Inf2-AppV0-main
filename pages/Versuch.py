import streamlit as st
from utils.data_manager import DataManager

data_manager = DataManager(fs_protocol='webdav', fs_root_folder="App/BMLD-Verdunnungsrechner")

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

with st.form("verdünnung_formular"):
    c1 = st.number_input("Eingangskonzentration (c1) in mol/L", min_value=0.0, step=0.1)
    v1 = st.number_input("Eingangsvolumen (V1) in L", min_value=0.0, step=0.1)
    c2 = st.number_input("Zielkonzentration (c2) in mol/L", min_value=0.0, step=0.1)
    
    submitted = st.form_submit_button("Berechnen")

if submitted:
    if c1 > 0 and v1 > 0 and c2 > 0 and c2 < c1:
        v2 = (c1 * v1) / c2  
        v_d = v2 - v1 

        st.success(f"Das benötigte Endvolumen (V2) ist: {v2:.3f} L")
        st.success(f"Das Verdünnungsvolumen (V_D) ist: {v_d:.3f} L")
    else:
        st.error("Bitte geben Sie gültige Werte ein. c2 muss kleiner als c1 sein und alle Werte müssen größer als 0 sein.")


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
        st.success(result["message"])
        

        record_dict = {
            "timestamp": helpers.ch_now(),  
            "c1": c1,
            "v1": v1,
            "c2": c2,
            "v2": result["v2"],
            "v_d": result["v_d"],
            "message": result["message"]
        }

        if 'data_df' not in st.session_state:
            st.session_state['data_df'] = []
   
        st.session_state['data_df'].append(record_dict)

    else:
        st.error(result["message"])






# Hintergrundfarbe

st.markdown(
    """
    <style>
        body, .stApp {
            background: radial-gradient(circle, #C6DE9B, #F9F9F9) !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Schriftfarbe

st.markdown("""
    <style>
        h1, h2, h3, h4, h5, h6, p, div {
            color: black !important;
        }
    </style>
    """, unsafe_allow_html=True)