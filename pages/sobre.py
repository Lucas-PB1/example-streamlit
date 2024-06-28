import streamlit as st

# Config
st.logo("static/logo.png")

st.title('Sobre o desenvolvimento')

st.markdown("Está Aplicação foi criada pelo desenvolvedor Lucas Soares Lima com fim de testar suas funcionalidades.")
st.image('static/dev.png', caption='Lucas Soares - Dev Full Stack')

# Sidebar
st.sidebar.write("StreamLit Application")