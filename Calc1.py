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
                width: 7%;           /* Reducir aún más el ancho de los botones */
                height: 20px;        /* Reducir la altura de los botones */
                font-size: 7px;      /* Reducir el tamaño del texto */
                margin: 0.5px;       /* Reducir más el margen/espacio entre botones */
                padding: 0px;        /* Eliminar relleno para minimizar espacio */
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    # Configurar el diseño basado en la orientación
    for i in range(0, len(buttons), 4):  # 4 columnas por fila
        cols = st.columns(4)
        for j, button in enumerate(buttons[i:i+4]):
            key = f"button-{button}-{i+j}"
            button_text = {
                'sqrt': '√',
                'pow': '^',
                'log': 'log',
                '*': 'X',
                '-': 'Rest',
                '+': 'Sum'
            }.get(button, button)
            cols[j].button(button_text, key=key, on_click=partial(append_expression, button) if button not in {'=', 'C'} else partial(operate, button))

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
