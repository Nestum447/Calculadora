import streamlit as st
from functools import partial

# Función de la calculadora
def calculator():
    st.title("Calculadora con st.selectbox")

    # Inicializar el estado de la expresión si no existe
    if 'expression' not in st.session_state:
        st.session_state['expression'] = ""

    # Grupos de botones organizados para la calculadora
    group1 = ['7', '8', '9', '/']
    group2 = ['4', '5', '6', '*']
    group3 = ['1', '2', '3', '-']
    group4 = ['0', '.', '=', '+']

    # Crear controles selectbox para cada grupo
    sel_group1 = st.selectbox("Seleccione", group1, key="group1")
    sel_group2 = st.selectbox("", group2, key="group2")
    sel_group3 = st.selectbox("", group3, key="group3")
    sel_group4 = st.selectbox("", group4, key="group4")

    # Crear un botón para añadir la selección a la expresión
    if st.button("Agregar"):
        append_expression(sel_group1)
        append_expression(sel_group2)
        append_expression(sel_group3)
        append_expression(sel_group4)

    # Mostrar la expresión en una caja de texto
    st.text_input("Expresión", st.session_state['expression'], key="expression_display", label_visibility="hidden")

# Función para agregar a la expresión
def append_expression(char):
    if char == '=':
        try:
            # Evaluar la expresión
            st.session_state['expression'] = str(eval(st.session_state['expression']))
        except Exception as e:
            st.session_state['expression'] = "Error"
    else:
        st.session_state['expression'] += str(char)

# Ejecutar la calculadora
if __name__ == "__main__":
    calculator()
