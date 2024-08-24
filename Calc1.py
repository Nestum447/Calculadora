import streamlit as st

# Crear columnas para organizar los botones
col1, col2, col3, col4 = st.columns(4)

# Primera fila de botones
with col1:
    st.button("7")
with col2:
    st.button("8")
with col3:
    st.button("9")
with col4:
    st.button("/")

# Segunda fila de botones
with col1:
    st.button("4")
with col2:
    st.button("5")
with col3:
    st.button("6")
with col4:
    st.button("*")

# Tercera fila de botones
with col1:
    st.button("1")
with col2:
    st.button("2")
with col3:
    st.button("3")
with col4:
    st.button("-")

# Cuarta fila de botones
with col1:
    st.button("0")
with col2:
    st.button(".")
with col3:
    st.button("=")
with col4:
    st.button("+")
