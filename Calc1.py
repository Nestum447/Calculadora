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
        ('7', 'lightblue'), ('8', 'lightblue'), ('9', 'lightblue'), ('/', 'orange'),
        ('4', 'lightblue'), ('5', 'lightblue'), ('6', 'lightblue'), ('*', 'orange'),
        ('1', 'lightblue'), ('2', 'lightblue'), ('3', 'lightblue'), ('-', 'orange'),
        ('C', 'red'), ('0', 'lightblue'), ('=', 'green'), ('+', 'orange'),
        ('sqrt', 'lightgreen'), ('pow', 'lightgreen'), ('log', 'lightgreen'), ('.', 'lightblue')
    ]

    # Crear un diseño en cuadrícula de 4 columnas para los botones
    button_grid = [buttons[i:i+4] for i in range(0, len(buttons), 4)]

    # Crear los botones con sus colores y eventos
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

            # Aplicar estilos y definir eventos para cada botón
            if button in {'=', 'C'}:
                cols[i].button(
                    button_text,
                    key=key,
                    on_click=partial(operate, button),
                    use_container_width=True
                )
            else:
                cols[i].button(
                    button_text,
                    key=key,
                    on_click=partial(append_expression, button),
                    use_container_width=True
                )

    # Mostrar la expresión en una caja de texto
    st.text_input("Expresión", st.session_state['expression'], key="expression_display")

# Ejecutar la calculadora
if __name__ == "__main__":
    calculator()
