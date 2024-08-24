import streamlit as st
import math
from functools import partial

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

# Función de la calculadora
def calculator():
    st.title("Calculadora Científica")

    # Inicializar el estado de la expresión si no existe
    if 'expression' not in st.session_state:
        st.session_state['expression'] = ""

    # Definir los botones y colores
    buttons = [
        ('7', 'lightblue'), ('8', 'lightblue'), ('9', 'lightblue'), ('/', 'orange'), ('sqrt', 'lightgreen'),
        ('4', 'lightblue'), ('5', 'lightblue'), ('6', 'lightblue'), ('*', 'orange'), ('pow', 'lightgreen'),
        ('1', 'lightblue'), ('2', 'lightblue'), ('3', 'lightblue'), ('-', 'orange'), ('log', 'lightgreen'),
        ('0', 'lightblue'), ('.', 'lightblue'), ('=', 'green'), ('+', 'orange'), ('C', 'red')
    ]

    # Crear un diseño en cuadrícula para los botones
    button_grid = [buttons[i:i+5] for i in range(0, len(buttons), 5)]

    # Crear botones con colores utilizando columnas de Streamlit
    for row in button_grid:
        cols = st.columns(len(row))
        for i, (button, color) in enumerate(row):
            key = f"button-{button}-{i}"
            button_text = {
                'sqrt': '√',
                'pow': '^',
                'log': 'log',
                '*': 'X',
                '-': 'Rest',
                '+': 'Sum'
            }.get(button, button)

            # Crear un botón con un estilo CSS personalizado
            custom_button = st.markdown(
                f"""
                <style>
                .button-{key} {{
                    background-color: {color};
                    color: white;
                    font-size: 20px;
                    padding: 15px 30px;
                    margin: 5px;
                    width: 100%;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    text-align: center;
                }}
                .button-{key}:hover {{
                    background-color: dark{color};
                }}
                </style>
                <button class="button-{key}" onclick="window.parent.postMessage({{button: '{button}'}}, '*')">{button_text}</button>
                """,
                unsafe_allow_html=True
            )

            if st.session_state.get("button", "") == button:
                if button in {'=', 'C'}:
                    operate(button)
                else:
                    append_expression(button)

    # Mostrar la expresión en una caja de texto
    st.text_input("Expresión", st.session_state['expression'], key="expression_display")

# Ejecutar la calculadora
if __name__ == "__main__":
    calculator()
