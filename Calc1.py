import streamlit as st

st.markdown(
    """
    <style>
    /* Asegurar que las columnas se mantengan en una fila en pantallas pequeñas */
    [data-testid="column"] {
        flex: 1 1 50%; /* Ocupa la mitad del ancho disponible */
        max-width: 50%; /* Limita el ancho máximo al 50% */
        min-width: 50%; /* Mantiene el ancho mínimo en 50% */
    }

    /* Ajustar tamaño de los botones en pantallas pequeñas */
    .stButton button {
        font-size: 14px; /* Ajustar el tamaño del texto */
        padding: 5px; /* Reducir el espacio interno */
    }

    /* Reducir el tamaño de la caja de texto en modo vertical */
    .stTextInput input {
        font-size: 14px; /* Ajustar el tamaño del texto */
        padding: 5px; /* Reducir el espacio interno */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Aquí va tu función para crear los botones
def create_two_columns():
    st.title("Calculadora en Vista Vertical")

    col1, col2 = st.columns(2)

    buttons_col1 = ["Botón 1", "Botón 2", "Botón 3", "Botón 4"]
    buttons_col2 = ["Botón A", "Botón B", "Botón C", "Botón D"]

    for i, text in enumerate(buttons_col1):
        col1.button(text, key=f"col1_button_{i}", use_container_width=True)

    for i, text in enumerate(buttons_col2):
        col2.button(text, key=f"col2_button_{i}", use_container_width=True)

if __name__ == "__main__":
    create_two_columns()
