import streamlit as st
from functools import partial

# Función de la calculadora
def calculator():
    st.title("Calculadora con 2 Columnas")

    # Inicializar el estado de la expresión si no existe
    if 'expression' not in st.session_state:
        st.session_state['expression'] = ""

    # Definir los botones en dos columnas
    buttons_col1 = ['7', '4', '1', '0']
    buttons_col2 = ['8', '5', '2', '.']
    buttons_col3 = ['9', '6', '3', '=']
    buttons_col4 = ['/', '*', '-', '+']

    # Crear un expander para contener los botones en dos columnas
    with st.expander("Controles"):
        col1, col2 = st.columns(2)

        # Mostrar los botones en la primera columna
        with col1:
            for button in buttons_col1 + buttons_col3:
                st.button(button, key=button, on_click=partial(append_expression, button))

        # Mostrar los botones en la segunda columna
        with col2:
            for button in buttons_col2 + buttons_col4:
                st.button(button, key=button, on_click=partial(append_expression, button))

    # Mostrar la expresión en una caja de texto
    st.text_input("Expresión", st.session_state['expression'], key="expression_display", label_visibility="hidden")

# Función para agregar a la expresión
def append_expression(char):
    st.session_state['expression'] += str(char)

# Ejecutar la calculadora
if __name__ == "__main__":
    calculator()
