import streamlit as st

st.title("Daten des Verdünnungsrechner")

if 'data_df' not in st.session_state or st.session_state['data_df'].empty:
    st.info('Keine Daten vorhanden. Berechnen Sie Ihre Verdünnung im Verdünnungsrechner.')
    st.stop()

data_df = st.session_state['data_df']

data_df = data_df.sort_values('timestamp', ascending=False)

st.dataframe(data_df)

if st.button("Zurück zur Startseite"):
    st.switch_page("Start.py")
if st.button("Zum Verdünnungsrechner"):
    st.switch_page("pages/1_Verdünnungsrechner.py")
if st.button("Zur Verdünnungsrechner-Grafik"):
    st.switch_page("pages/3_Verdünnungsrechner-Grafik.py")


# Hintergrundfarbe

import streamlit as st

st.markdown(
    """
    <style>
        .stApp {
            background: radial-gradient(circle, #C6DE9B, #F9F9F9);
        } 
    </style>
    """,
    unsafe_allow_html=True
)
