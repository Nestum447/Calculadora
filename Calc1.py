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

    # Ajustar las columnas a 4 por fila
    button_grid = [buttons[i:i+4] for i in range(0, len(buttons), 4)]

    for row in button_grid:
        cols = st.columns(len(row))
        for i, button in enumerate(row):
            key = f"button-{button}-{i}"
            
            # Asegurarse de que el botón tenga el texto correcto
            button_text = {
                'sqrt': '√',
                'pow': '^',
                'log': 'log',
                '*': 'X',
                '-': 'Rest',
                '+': 'Sum'
            }.get(button, button)

            # Crear el botón con el texto adecuado
            if button in {'=', 'C'}:
                cols[i].button(button_text, key=key, on_click=partial(operate, button))
            else:
                cols[i].button(button_text, key=key, on_click=partial(append_expression, button))

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
