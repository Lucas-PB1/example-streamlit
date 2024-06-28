import time
import streamlit as st
from functions import calc as c
from functions import connect as db

# Config
st.logo("static/logo.png")

st.title('Streamlit Example Application')
st.write("Está Aplicação tem por fim criar dados de forma dinamica com uso de *Streamlit*")

option = st.selectbox(
    "Selecione a Aplicação que deseja testar",
    ("Calculadora", "Idade", "Diferença de Data e hora"),
    index=None,
    placeholder="Selecione uma funcionalidade.")

match option:
    case "Calculadora":
        with st.form("my_form"):
            n1 = st.number_input("Número 1")
            n2 = st.number_input("Número 2")
            typeCalc = st.selectbox("Calcule:", ("Multiplicação", "Subtração", "Adição", "Divisão"))
            
            submitted = st.form_submit_button("Enviar")
            if submitted: st.write("Resultado: " + c.calculator(n1, n2, typeCalc) + ".")
    case "Idade":
        with st.form("my_form"):
            birthdate = st.date_input("Data de nascimento")
            
            submitted = st.form_submit_button("Enviar")
            if submitted: st.write("Idade Atual: " + c.idade(birthdate) + " anos.")
    case "Diferença de Data e hora":
        with st.form("my_form"):
            d1 = st.date_input("Primeira data")
            d2 = st.date_input("Segunda data")
           
            submitted = st.form_submit_button("Enviar")
            if submitted:st.write("A diferença entre duas data é: " + c.difDatas(d1, d2))

@st.experimental_dialog("Avalie o site!")
def avalie():
    st.write("Avalie sua experiência com Streamlit:")
    nome = st.text_input("Seu Nome:")
    result = st.selectbox("Escolha:", ("Ótima", "Boa", "Mediana", "Ruim"), index=None, placeholder="Avaliação")
    
    if result == "Ótima": result = 4
    if result == "Boa": result = 3
    if result == "Mediana": result = 2
    if result == "Ruim": result = 1

    if st.button("Enviar"):
        conn = db.connect()
        conn.cursor().execute(f"INSERT INTO avaliacoes (nome, nota) VALUES (%s, %s)", (nome, result))
        conn.commit()
        conn.close()
        
        progress_text = "Enviando Avaliação."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()
        st.rerun()
 
if st.button("Avalie a aplicação!"): avalie()

# Sidebar
st.sidebar.write("StreamLit Application")
