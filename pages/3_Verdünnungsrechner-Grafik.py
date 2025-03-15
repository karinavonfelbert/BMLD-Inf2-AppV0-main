import streamlit as st

st.title("Grafik des Verdünnungsrechners")

st.write("Hier sehen Sie die Grafik des Verdünnungsrechners.")


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
