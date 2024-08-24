import streamlit as st
from functools import partial

# Función de la calculadora
def calculator():
    st.title("Calculadora con st.select_slider")

    # Inicializar el estado de la expresión si no existe
    if 'expression' not in st.session_state:
        st.session_state['expression'] = ""

    # Grupos de botones organizados para la calculadora
    buttons = ['7', '8', '9', '/',
               '4', '5', '6', '*',
               '1', '2', '3', '-',
               '0', '.', '=', '+']

    # Crear un slider para seleccionar un botón
    selected_button = st.select_slider("Seleccione un botón", options=buttons)

    # Crear un botón para añadir la selección a la expresión
    if st.button("Agregar"):
        append_expression(selected_button)

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
