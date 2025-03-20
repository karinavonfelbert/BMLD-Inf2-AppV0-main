import streamlit as st
import pandas as pd

st.title("Verdünnungsrechner Verlauf")

# Sicherstellen, dass die Daten existieren
if "data_df" not in st.session_state or st.session_state["data_df"].empty:
    st.info("Keine gespeicherten Verdünnungsdaten vorhanden. Gehen Sie zur Berechnungsseite, um Werte einzugeben.")
    st.stop()

# Daten abrufen
data_df = st.session_state["data_df"]

# Debugging: Prüfen, welche Spalten existieren
st.write("Verfügbare Spalten:", data_df.columns.tolist())

# Sicherstellen, dass alle benötigten Spalten existieren
required_columns = ["timestamp", "c1", "v1", "c2", "V2"]
missing_columns = [col for col in required_columns if col not in data_df.columns]

if missing_columns:
    st.error(f"Fehlende Spalten in data_df: {', '.join(missing_columns)}")
    st.stop()

# **Daten nach Zeitachse indexieren**
data_df = data_df.set_index("timestamp")

# **Diagramme anzeigen**
st.line_chart(data=data_df["c1"], use_container_width=True)
st.caption("Eingangskonzentration (c₁) über Zeit (mol/L)")

st.line_chart(data=data_df["v1"], use_container_width=True)
st.caption("Eingangsvolumen (V₁) über Zeit (L)")

st.line_chart(data=data_df["c2"], use_container_width=True)
st.caption("Zielkonzentration (c₂) über Zeit (mol/L)")

st.line_chart(data=data_df["V2"], use_container_width=True)
st.caption("Endvolumen (V₂) über Zeit (L)")

# **Optionale Tabelle zur Kontrolle**
st.write("Gespeicherte Verdünnungsdaten:")
st.dataframe(data_df)
