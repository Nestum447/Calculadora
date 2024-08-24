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
    buttons = [
        '7', '8', '9', '/', 
        '4', '5', '6', '*', 
        '1', '2', '3', '-', 
        '0', '.', '=', '+',
        'sqrt', 'pow', 'log', 'C'
    ]

    # CSS para el modo horizontal
    if not is_vertical:
        st.markdown(
            """
            <style>
            .stButton > button {
                width: 100%;
                height: 50px;
                font-size: 18px;
            }
            .stTextInput input {
                width: 100%;
                font-size: 18px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        # CSS para el modo vertical
        st.markdown(
            """
            <style>
            .stButton > button {
                width: 10%;           /* Establece el ancho de los botones a 100% del contenedor */
                height: 10px;         /* Ajusta la altura de los botones */
                font-size: 7px;      /* Ajusta el tamaño del texto en los botones */
                margin: 0.0000px;          /* Reduce el espacio entre los botones */
                padding: 0px;        /* Elimina el relleno para minimizar el espacio */
            }
            /* Ajusta el espaciado entre columnas */
            .stColumn {
                padding: 0;
            }
            .stTextInput input {
                width: 20%;           /* Reduce el tamaño del cuadro de expresión */
                font-size: 10px;      /* Ajusta el tamaño del texto en el cuadro de expresión */
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    # Configurar el diseño basado en la orientación
    num_cols = 4  # Número de columnas deseado
    num_rows = (len(buttons) + num_cols - 1) // num_cols  # Calcula el número de filas necesarias

    for row in range(num_rows):
        cols = st.columns(num_cols)
        for col in range(num_cols):
            index = row * num_cols + col
            if index < len(buttons):
                button = buttons[index]
                key = f"button-{button}-{index}"
                button_text = {
                    'sqrt': '√',
                    'pow': '^',
                    'log': 'log',
                    '*': 'X',
                    '-': 'Rest',
                    '+': 'Sum'
                }.get(button, button)
                if button in {'=', 'C'}:
                    cols[col].button(button_text, key=key, on_click=partial(operate, button))
                else:
                    cols[col].button(button_text, key=key, on_click=partial(append_expression, button))

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
