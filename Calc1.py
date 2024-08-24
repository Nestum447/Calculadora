import streamlit as st
from functools import partial

# Función de la calculadora
def calculator():
    st.title("Calculadora con 2 Columnas Fijas")

    # Inicializar el estado de la expresión si no existe
    if 'expression' not in st.session_state:
        st.session_state['expression'] = ""

    # Definir los botones
    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+'
    ]

    # Aplicar estilo CSS personalizado
    st.markdown(
        """
        <style>
        .button-grid {
            display: grid;
            grid-template-columns: 1fr 1fr; /* Dos columnas */
            gap: 10px; /* Espacio entre botones */
        }
        .stButton > button {
            width: 100%; /* Botones ocupan el ancho completo de la columna */
            height: 50px; /* Ajusta la altura de los botones */
            font-size: 18px; /* Ajusta el tamaño del texto */
        }
        .stTextInput > div > input {
            font-size: 18px;
            height: 50px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Crear un contenedor para los botones
    st.markdown('<div class="button-grid">', unsafe_allow_html=True)
    
    for button in buttons:
        st.button(button, key=button, on_click=partial(append_expression, button))
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Mostrar la expresión en una caja de texto
    st.text_input("Expresión", st.session_state['expression'], key="expression_display", label_visibility="hidden")

# Función para agregar a la expresión
def append_expression(char):
    st.session_state['expression'] += str(char)

# Ejecutar la calculadora
if __name__ == "__main__":
    calculator()
