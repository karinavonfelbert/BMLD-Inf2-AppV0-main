import streamlit as st

st.title("Daten des Verdünnungsrechner")

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Verdünnungswerte vorhanden. Berechnen Sie Ihre Verdünnungen auf der Startseite.')
    st.stop()

data_df = data_df.sort_values('timestamp', ascending=False)
st.dataframe(data_df)