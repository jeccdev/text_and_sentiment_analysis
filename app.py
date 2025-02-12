import string  # Para manejar caracteres de puntuación
import tkinter as tk  # Para la interfaz gráfica
from tkinter import scrolledtext  # Para el widget de texto con desplazamiento
from textblob import TextBlob  # Para el análisis de sentimiento del texto (funciona mejor en inglés)

def analizar_texto():
    """
    Función que analiza el texto ingresado por el usuario.
    Realiza las siguientes tareas:
    1. Convierte el texto a minúsculas y elimina la puntuación.
    2. Calcula la frecuencia de cada palabra en el texto.
    3. Encuentra la palabra más frecuente (palabra modal).
    4. Analiza el sentimiento del texto (positivo, negativo o neutral).
    5. Muestra los resultados en el área de texto de salida.
    """
    texto = entrada_texto.get("1.0", tk.END).strip().lower()  # Obtener texto del usuario y convertir a minúsculas
    texto = texto.translate(str.maketrans("", "", string.punctuation))  # Eliminar puntuación

    palabras = texto.split()  # Separar el texto en palabras
    frecuencia = {}  # Diccionario para almacenar la frecuencia de palabras

    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1  # Contar frecuencia de cada palabra

    palabra_modal = max(frecuencia, key=frecuencia.get) if frecuencia else "N/A"  # Palabra más repetida
    analisis_sentimiento = TextBlob(texto).sentiment  # Analizar sentimiento
    polaridad = analisis_sentimiento.polarity  # Obtener polaridad del sentimiento
    sentimiento = "Positivo" if polaridad > 0 else "Negativo" if polaridad < 0 else "Neutral"  # Determinar sentimiento

    # Formatear los resultados para mostrarlos en la interfaz gráfica
    resultado_texto = f"Total de palabras: {len(palabras)}\n"
    resultado_texto += f"Palabra modal: {palabra_modal}\n\nFrecuencia de palabras:\n"

    for palabra, freq in frecuencia.items():
        resultado_texto += f"- {palabra}: {freq}\n"

    resultado_texto += f"\nSentimiento: {sentimiento}\nPolaridad: {polaridad:.2f}"

    # Mostrar resultados en el widget de texto
    resultado_label.config(state=tk.NORMAL)
    resultado_label.delete("1.0", tk.END)
    resultado_label.insert(tk.INSERT, resultado_texto)
    resultado_label.config(state=tk.DISABLED)

def nuevo_texto():
    """
    Función que limpia el área de entrada y el área de resultados
    para permitir un nuevo análisis de texto.
    """
    entrada_texto.delete("1.0", tk.END)  # Limpiar el área de entrada
    resultado_label.config(state=tk.NORMAL)
    resultado_label.delete("1.0", tk.END)  # Limpiar el área de resultados
    resultado_label.config(state=tk.DISABLED)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Análisis de texto y sentimiento")  # Título de la ventana
ventana.geometry("500x550")  # Tamaño de la ventana

# Etiqueta para indicar al usuario que ingrese un texto
tk.Label(ventana, text="Ingrese un texto:", font=("Arial", 12)).pack(pady=5)

# Área de texto con scroll para ingresar el texto a analizar
entrada_texto = scrolledtext.ScrolledText(ventana, width=50, height=5)
entrada_texto.pack(pady=5)

# Botón para analizar el texto ingresado
btn_analizar = tk.Button(
    ventana, text="Analizar", command=analizar_texto, font=("Arial", 12), 
    bg="#4CAF50", fg="white"  # Color verde para indicar acción positiva
)
btn_analizar.pack(pady=5)

# Botón para limpiar los campos y permitir un nuevo análisis
btn_nuevo = tk.Button(
    ventana, text="Nuevo Texto", command=nuevo_texto, font=("Arial", 12), 
    bg="#FFA000", fg="white"  # Color naranja para resaltar la función de reinicio
)
btn_nuevo.pack(pady=5)

# Etiqueta para mostrar los resultados del análisis
tk.Label(ventana, text="Resultados:", font=("Arial", 12)).pack(pady=5)

# Área de texto con scroll para mostrar los resultados del análisis
resultado_label = scrolledtext.ScrolledText(ventana, width=50, height=10, state=tk.DISABLED)
resultado_label.pack(pady=5)

# Botón para cerrar la aplicación
btn_cerrar = tk.Button(
    ventana, text="Cerrar", command=ventana.destroy, font=("Arial", 12), 
    bg="#D32F2F", fg="white"  
)
btn_cerrar.pack(pady=10)

# Iniciar la interfaz gráfica
ventana.mainloop()
