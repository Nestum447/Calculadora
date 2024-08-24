
import tkinter as tk

# Función para actualizar la entrada
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")

# Crear la entrada
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Definir los botones y sus colores
buttons = [
    ('7', 'lightblue'), ('8', 'lightblue'), ('9', 'lightblue'), ('/', 'orange'),
    ('4', 'lightblue'), ('5', 'lightblue'), ('6', 'lightblue'), ('*', 'orange'),
    ('1', 'lightblue'), ('2', 'lightblue'), ('3', 'lightblue'), ('-', 'orange'),
    ('C', 'red'), ('0', 'lightblue'), ('=', 'green'), ('+', 'orange')
]

# Crear los botones y agregarlos a la cuadrícula
row, col = 1, 0
for (text, color) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), bg=color, command=lambda t=text: click(t))
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Ejecutar la aplicación
root.mainloop()
En este código:

Se crea una ventana principal con tkinter.
Se añade un Entry para mostrar los números y resultados.
Se definen los botones con sus respectivos colores.
Cada botón se crea con el color correspondiente y se añade a la cuadrícula.
Se maneja el evento de clic para actualizar la entrada o calcular el resultado.
Puedes ajustar los colores y el diseño según tus preferencias. ¿Necesitas algo más específico?





Dijiste:
a este codigo agregarle colores a los botones: import streamlit as st
import math
from functools import partial

# Función de la calculadora
def calculator():
    st.title("Calculadora Científica")

    # Inicializar el estado de la expresión si no existe
    if 'expression' not in st.session_state:
        st.session_state['expression'] = ""

    # Definir los botones
    buttons = [
        '7', '8', '9', '/', 'sqrt', 
        '4', '5', '6', '*', 'pow', 
        '1', '2', '3', '-', 'log',
        '0', '.', '=', '+', 'C'
    ]

    # Crear un diseño en cuadrícula para los botones
    button_grid = [buttons[i:i+5] for i in range(0, len(buttons), 5)]

    for row in button_grid:
        cols = st.columns(len(row))
        for i, button in enumerate(row):
            key = f"button-{button}-{i}"
            
            # Asegurarse de que el botón tenga el texto correcto
            button_text = {
                'sqrt': '√',
                'pow': '^',
                'log': 'log',
                '*': 'X',
                '-': 'Rest',
                '+': 'Sum'


            }.get(button, button)

            # Crear el botón con el texto adecuado
            if button in {'=', 'C'}:
                cols[i].button(button_text, key=key, on_click=partial(operate, button))
            else:
                cols[i].button(button_text, key=key, on_click=partial(append_expression, button))

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

# Ejecutar la calculadora
if __name__ == "__main__":
    calculator()
