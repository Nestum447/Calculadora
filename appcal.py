import streamlit as st
import math

# Función de la calculadora
def calculator():
    st.title("Calculadora Científica")

    # Crear dos columnas para simular la disposición de una calculadora física
    col1, col2, col3, col4 = st.columns(4)

    # Usar una caja de texto para mostrar el resultado
    result = st.empty()

    # Variables de entrada
    expr = st.text_input("Introduce tu expresión:", key="expression")

    # Funciones disponibles
    buttons = [
        '7', '8', '9', '/', 'sqrt', 
        '4', '5', '6', '*', 'pow', 
        '1', '2', '3', '-', 'log',
        '0', '.', '=', '+', 'C'
    ]

    # Mostrar los botones
    for i in range(0, len(buttons), 5):
        col1.button(buttons[i], on_click=lambda: append_expression(buttons[i]))
        col2.button(buttons[i+1], on_click=lambda: append_expression(buttons[i+1]))
        col3.button(buttons[i+2], on_click=lambda: append_expression(buttons[i+2]))
        col4.button(buttons[i+3], on_click=lambda: append_expression(buttons[i+3]))

    # Evaluar la expresión cuando se presiona '='
    if st.button('=', key='equal'):
        try:
            # Reemplazar expresiones para funciones científicas
            expr = expr.replace('sqrt', 'math.sqrt')
            expr = expr.replace('pow', '**')
            expr = expr.replace('log', 'math.log10')

            result.success(eval(expr))
        except:
            result.error("Error en la expresión")

    # Limpiar la expresión cuando se presiona 'C'
    if st.button('C', key='clear'):
        st.session_state.expression = ""

# Función auxiliar para agregar la expresión
def append_expression(char):
    if 'expression' not in st.session_state:
        st.session_state.expression = ""
    st.session_state.expression += str(char)

# Ejecutar la calculadora
if __name__ == "__main__":
    calculator()
