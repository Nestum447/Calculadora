import streamlit as st
from functools import partial

# Función de la calculadora
def calculator():
    st.title("Calculadora con Controles de Selección")

    # Inicializar el estado de la expresión si no existe
    if 'expression' not in st.session_state:
        st.session_state['expression'] = ""

    # Opciones de botones organizadas en grupos
    options_group_1 = ['7', '8', '9', '/']
    options_group_2 = ['4', '5', '6', '*']
    options_group_3 = ['1', '2', '3', '-']
    options_group_4 = ['0', '.', '=', '+']

    # Crear controles de selección para cada grupo
    selection_1 = st.radio("Seleccione:", options_group_1, horizontal=True, key="group1")
    selection_2 = st.radio("", options_group_2, horizontal=True, key="group2")
    selection_3 = st.radio("", options_group_3, horizontal=True, key="group3")
    selection_4 = st.radio("", options_group_4, horizontal=True, key="group4")

    # Almacenar las selecciones
    selections = [selection_1, selection_2, selection_3, selection_4]

    # Crear un botón de confirmación para aplicar la selección
    if st.button("Aplicar"):
        for selection in selections:
            append_expression(selection)

    # Mostrar la expresión en una caja de texto
    st.text_input("Expresión", st.session_state['expression'], key="expression_display", label_visibility="hidden")

# Función para agregar a la expresión
def append_expression(char):
    st.session_state['expression'] += str(char)

# Ejecutar la calculadora
if __name__ == "__main__":
    calculator()
