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

    # Dividir los botones en filas
    button_grid = [buttons[i:i + 4] for i in range(0, len(buttons), 4)]

    # Ajustar la altura y el tamaño del texto de los botones
    button_height = 40  # Ajusta la altura del botón
    button_font_size = 20  # Ajusta el tamaño de la fuente

    # Añadir estilo personalizado para los botones
    st.markdown(
        f"""
        <style>
        .stButton > button {{
            height: {button_height}px;
            font-size: {button_font_size}px;
            margin: 2px;
        }}
        .stTextInput > div > input {{
            font-size: {button_font_size}px;
            height: {button_height}px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Mostrar la expresión en una caja de texto
    st.text_input("Expresión", st.session_state['expression'], key="expression_display", label_visibility="hidden")

    # Mostrar los botones en una cuadrícula
    for row in button_grid:
        cols = st.columns(4)  # Forzar siempre 4 columnas
        for i, button in enumerate(row):
            key = f"button-{button}-{i}"
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
