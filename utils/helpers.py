import streamlit as st
from datetime import datetime
import pandas as pd

def init_session_state():
    if 'user' not in st.session_state:
        st.session_state.user = None
    if 'examens' not in st.session_state:
        st.session_state.examens = []
    if 'conflits' not in st.session_state:
        st.session_state.conflits = []
    if 'generation_time' not in st.session_state:
        st.session_state.generation_time = None

def check_authentication():
    if st.session_state.user is None:
        st.warning("Vous devez vous connecter d'abord")
        st.switch_page("pages/Connexion.py")
        st.stop()

def logout():
    st.session_state.user = None
    st.session_state.examens = []
    st.session_state.conflits = []
    st.switch_page("pages/Connexion.py")

def format_date(date_str):
    try:
        dt = datetime.strptime(str(date_str), '%Y-%m-%d %H:%M:%S')
        return dt.strftime('%d/%m/%Y à %H:%M')
    except:
        return date_str

def export_to_csv(data, filename):
    csv = data.to_csv(index=False)
    st.download_button(
        label="Télécharger CSV",
        data=csv,
        file_name=filename,
        mime="text/csv"
    )