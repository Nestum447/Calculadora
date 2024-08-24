import streamlit as st
from functools import partial

# Función de la calculadora
def calculator():
    st.title("Calculadora con 2 Columnas Fijas")

    # Inicializar el estado de la expresión si no existe
    if 'expression' not in st.session_state:
        st.session_state['expression'] = ""

    # Definir los botones en dos columnas
    buttons = [
        ['7', '8'],
        ['4', '5'],
        ['1', '2'],
        ['0', '.'],
        ['9', '/'],
        ['6', '*'],
        ['3', '-'],
        ['=', '+']
    ]

    # Crear el layout de las columnas manualmente
    for row in buttons:
        col1, col2 = st.columns(2)
        with col1:
            st.button(row[0], key=row[0], on_click=partial(append_expression, row[0]))
        with col2:
            st.button(row[1], key=row[1], on_click=partial(append_expression, row[1]))

    # Mostrar la expresión en una caja de texto
    st.text_input("Expresión", st.session_state['expression'], key="expression_display", label_visibility="hidden")

# Función para agregar a la expresión
def append_expression(char):
    st.session_state['expression'] += str(char)

# Ejecutar la calculadora
if __name__ == "__main__":
    calculator()
