import streamlit as st
import pandas as pd
import numpy as np
import time

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

# Tabela
# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))

# Tabela Complexa
# dataframe = np.random.randn(10, 20)
# st.dataframe(dataframe)

# Colunas Com Cores
# dataframe = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))
# st.dataframe(dataframe.style.highlight_max(axis=0))

# Metodo de tabelas sem função de visualização
# dataframe = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))
# st.table(dataframe)

# Line CHART
# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])
# st.line_chart(chart_data)

# MAP
# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])
# st.map(map_data)

# Widget
# x = st.slider('x')  #
# st.write(x, 'squared is', x * x)

# Inputs
# st.text_input("Your name", key="name")
# st.session_state.name

# Checkbox
# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])
#     chart_data


# Select
# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })

# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])

# 'You selected: ', option

# Button
# left_column, right_column = st.columns(2)
# left_column.button('Press me!')

# Radio
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")

# Loading
# 'Starting a long computation...'
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)
# '...and now we\'re done!'

# States
# if "counter" not in st.session_state:
#     st.session_state.counter = 0

# st.session_state.counter += 1

# st.header(f"This page has run {st.session_state.counter} times.")
# st.button("Run it again")

# Color Picker
# if "df" not in st.session_state:
#     st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

# st.header("Choose a datapoint color")
# color = st.color_picker("Color", "#FF0000")
# st.divider()
# st.scatter_chart(st.session_state.df, x="x", y="y", color=color)

# Conexão com banco de dados
# conn = st.connection("my_database")
# df = conn.query("select * from migrations")
# st.dataframe(df)

# Imagem
# with st.echo():
#     st.title("CAT")
#     st.markdown("[![Click me](app/static/cat.png)](https://streamlit.io)")