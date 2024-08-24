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

    # CSS común para ambos modos
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

    # Configurar el diseño basado en la orientación
    if is_vertical:
        st.write("Modo Vertical Detectado")
        for i in range(0, len(buttons), 4):  # 4 columnas por fila en modo vertical
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
    else:
        st.write("Modo Horizontal Detectado")
        for i in range(0, len(buttons), 4):  # 4 columnas por fila en modo horizontal
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

# JavaScript para detectar la orientación
st.markdown(
    """
    <script>
    function sendOrientation() {
        var width = window.innerWidth;
        var height = window.innerHeight;
        if (width < height) {
            // Modo vertical
            Streamlit.setComponentValue(true);
        } else {
            // Modo horizontal
            Streamlit.setComponentValue(false);
        }
    }
    window.addEventListener('resize', sendOrientation);
    document.addEventListener('DOMContentLoaded', sendOrientation);
    </script>
    """,
    unsafe_allow_html=True
)

# Leer el valor de la orientación (vertical: True, horizontal: False)
is_vertical = st.experimental_get_query_params().get("orientation", ["false"])[0] == "true"

# Ejecutar la calculadora con la orientación correcta
if __name__ == "__main__":
    calculator(is_vertical)
