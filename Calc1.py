import streamlit as st

def create_two_columns():
    st.title("Dos Columnas en Vista Vertical")

    # Crear dos columnas en disposición vertical
    col1, col2 = st.columns(2)

    # Ajustar el tamaño y el espaciado de los botones
    button_kwargs = {
        "key": "button",
        "use_container_width": True
    }

    # Lista de botones para cada columna
    buttons_col1 = ["Botón 1", "Botón 2", "Botón 3", "Botón 4"]
    buttons_col2 = ["Botón A", "Botón B", "Botón C", "Botón D"]

    # Agregar botones a la primera columna
    with col1:
        for text in buttons_col1:
            st.button(text, **button_kwargs)

    # Agregar botones a la segunda columna
    with col2:
        for text in buttons_col2:
            st.button(text, **button_kwargs)

if __name__ == "__main__":
    create_two_columns()
