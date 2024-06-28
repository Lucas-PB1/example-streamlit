import streamlit as st
from functions import calc;

st.logo("static/logo.png")

st.title('Avaliações')
st.markdown("Ultimas avaliações da aplicação.")

conn = st.connection('db')
data = conn.query('select nome, nota from avaliacoes')

styled_data = data.style.map(calc.color_notes, subset=['nota'])
st.table(styled_data)

# Sidebar
st.sidebar.write("StreamLit Application")