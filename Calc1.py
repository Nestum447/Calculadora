import streamlit as st
import math
from functools import partial

# Función de la calculadora
def calculator(is_vertical):
    st.title("Calculadora Científica")

    # Inicializar el estado de la expresión si no existe
    if 'expression' not in st.session_state:
        st.session_state['expression'] = ""

    # Definir los botones
    buttons_horizontal = [
        '7', '8', '9', '/', 'sqrt', 
        '4', '5', '6', '*', 'pow', 
        '1', '2', '3', '-', 'log',
        '0', '.', '=', '+', 'C'
    ]

    buttons_vertical = [
        '7', '8', '9', '/', 
        '4', '5', '6', '*', 
        '1', '2', '3', '-', 
        'sqrt', 'pow', 'log', '+',
        '0', '.', '=', 'C'
    ]

    # Elegir los botones según la orientación
    buttons = buttons_vertical if is_vertical else buttons_horizontal

    # Configurar el número de columnas
    num_cols = 4

    # Crear un diseño en cuadrícula para los botones
    for i in range(0, len(buttons), num_cols):
        cols = st.columns(num_cols)
        for j, button in enumerate(buttons[i:i+num_cols]):
            key = f"button-{button}-{i+j}"
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
                cols[j].button(button_text, key=key, on_click=partial(operate, button))
            else:
                cols[j].button(button_text, key=key, on_click=partial(append_expression, button))

    # Mostrar la expresión en una caja de texto con tamaño reducido en modo vertical
    text_size = "20%" if is_vertical else "100%"
    st.text_input("Expresión", st.session_state['expression'], key="expression_display", label_visibility="hidden", disabled=True)

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

# Opción de selección manual
orientation = st.selectbox(
    "Selecciona el modo de visualización:",
    ("Horizontal", "Vertical")
)

# Determinar la orientación seleccionada
is_vertical = orientation == "Vertical"

# Ejecutar la calculadora con la orientación seleccionada
if __name__ == "__main__":
    calculator(is_vertical)
