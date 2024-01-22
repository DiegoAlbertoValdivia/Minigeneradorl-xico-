import tkinter as tk
from tkinter import scrolledtext
import re

def es_numero_real(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False

def analizador_lexico(texto):
    patron_identificador = r'[a-zA-Z_]\w*'
    patron_numero_real = r'\d+\.\d+'

    identificadores = list(set(re.findall(patron_identificador, texto)))
    numeros_reales = [num for num in re.findall(patron_numero_real, texto) if es_numero_real(num)]

    return identificadores, numeros_reales

def analizar_texto():
    texto_entrada = entrada_texto.get("1.0", tk.END)
    identificadores, numeros_reales = analizador_lexico(texto_entrada)

    lista_resultados.delete(1.0, tk.END)

    for identificador in identificadores:
        lista_resultados.insert(tk.END, f"{identificador:<20} | Identificador\n")

    for numero_real in numeros_reales:
        lista_resultados.insert(tk.END, f"{numero_real:<20} | Número real\n")

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Analizador Léxico")

etiqueta_texto = tk.Label(ventana, text="Ingrese el texto:")
etiqueta_texto.pack()

entrada_texto = scrolledtext.ScrolledText(ventana, width=40, height=10)
entrada_texto.pack()

boton_analizar = tk.Button(ventana, text="Analizar", command=analizar_texto)
boton_analizar.pack()

lista_resultados = scrolledtext.ScrolledText(ventana, width=50, height=10, wrap=tk.WORD)
lista_resultados.pack()

ventana.mainloop()
