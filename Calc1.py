import streamlit as st

def create_two_columns():
    st.title("Dos Columnas en Vista Vertical")

    # Crear dos columnas
    col1, col2 = st.columns(2)

    # Lista de botones para cada columna con identificadores únicos
    buttons_col1 = ["Botón 1", "Botón 2", "Botón 3", "Botón 4"]
    buttons_col2 = ["Botón A", "Botón B", "Botón C", "Botón D"]

    # Agregar botones a la primera columna
    for i, text in enumerate(buttons_col1):
        col1.button(text, key=f"col1_button_{i}", use_container_width=True)

    # Agregar botones a la segunda columna
    for i, text in enumerate(buttons_col2):
        col2.button(text, key=f"col2_button_{i}", use_container_width=True)

if __name__ == "__main__":
    create_two_columns()
