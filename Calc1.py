import streamlit as st

def create_two_columns_fixed():
    st.title("Calculadora en Vista Vertical")

    # Botones en pares para dos columnas
    buttons = [("Botón 1", "Botón A"), 
               ("Botón 2", "Botón B"), 
               ("Botón 3", "Botón C"), 
               ("Botón 4", "Botón D")]

    # Crear una fila de columnas para cada par de botones
    for i, (btn1, btn2) in enumerate(buttons):
        col1, col2 = st.columns(2)
        col1.button(btn1, key=f"col1_button_{i}", use_container_width=True)
        col2.button(btn2, key=f"col2_button_{i}", use_container_width=True)

if __name__ == "__main__":
    create_two_columns_fixed()
