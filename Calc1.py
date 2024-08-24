import streamlit as st
import math
from functools import partial

# Función de la calculadora
def calculator():
    st.title("Calculadora Científica")

    # Inicializar el estado de la expresión si no existe
    if 'expression' not in st.session_state:
        st.session_state['expression'] = ""

    # Definir los botones
    buttons = [
        '7', '8', '9', '/', 'sqrt', 
        '4', '5', '6', '*', 'pow', 
        '1', '2', '3', '-', 'log',
        '0', '.', '=', '+', 'C'
    ]

    # CSS para ajustar el comportamiento en pantallas pequeñas
    st.markdown(
        """
        <style>
        /* Contenedor de botones usando flexbox */
        .button-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
        }
        .button-container > div {
            flex: 1 1 23%; /* Asegura 4 botones por fila */
            margin: 5px;
        }
        button {
            width: 100%;
            height: 50px;
            font-size: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Crear el contenedor de botones
    st.markdown("<div class='button-container'>", unsafe_allow_html=True)
    
    for button in buttons:
        button_text = {
            'sqrt': '√',
            'pow': '^',
            'log': 'log',
            '*': 'X',
            '-': 'Rest',
            '+': 'Sum'
        }.get(button, button)

        # Crear cada botón con su contenedor
        st.markdown(f"<div>{st.button(button_text, key=f'button-{button}')}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Mostrar la expresión en una caja de texto
    st.text_input("Expresión", st.session_state['expression'], key="expression_display")

# Función para agregar a la expresión
def append_expression(char):
    if char == 'sqrt':
        st.session_state['expression'] += 'sqrt('
    elif char == 'pow':
        st.session_state['expression'] += '**'
    elif char == 'log':
        st.session_state['expression'] += 'log10('
    else:
        st.session_state['expression'] += str(char)

# Función para operar en la expresión
def operate(button):
    if button == '=':
        try:
            expr = st.session_state['expression']
            expr = expr.replace('sqrt(', 'math.sqrt(')
            expr = expr.replace('log10(', 'math.log10(')
            st.session_state['expression'] = str(eval(expr))
        except Exception as e:
            st.session_state['expression'] = f"Error: {e}"
    elif button == 'C':
        st.session_state['expression'] = ""

# Ejecutar la calculadora
if __name__ == "__main__":
    calculator()
