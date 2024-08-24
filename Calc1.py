import streamlit as st

def create_two_vertical_columns():
    st.title("Dos Columnas Verticales")

    # Crear dos columnas en disposición vertical
    col1, col2 = st.columns(2)

    # Ajustar el tamaño y el espaciado de los botones
    button_kwargs = {
        "key": "button",
        "use_container_width": True
    }

    # Agregar botones a la primera columna
    with col1:
        st.button("Botón 1", **button_kwargs)
        st.button("Botón 2", **button_kwargs)
        st.button("Botón 3", **button_kwargs)
        st.button("Botón 4", **button_kwargs)

    # Agregar botones a la segunda columna
    with col2:
        st.button("Botón A", **button_kwargs)
        st.button("Botón B", **button_kwargs)
        st.button("Botón C", **button_kwargs)
        st.button("Botón D", **button_kwargs)

# Ejecutar la función para mostrar dos columnas verticales
if __name__ == "__main__":
    create_two_vertical_columns()
