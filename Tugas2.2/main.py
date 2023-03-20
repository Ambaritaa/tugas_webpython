import pandas as pd
import streamlit as st

st.title('Pertemuan Lima Latihan 2 - Menghubungkan Database Google Sheets ke Streamlit')

@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])

st.table(df)