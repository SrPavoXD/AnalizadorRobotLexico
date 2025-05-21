import tkinter as tk
from tkinter import scrolledtext
from analizador import AnalizadorLexico
from analizador_sintactico import AnalizadorSintactico

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico y Sintáctico")

        # Cuadro de entrada de texto
        self.texto = scrolledtext.ScrolledText(root, width=70, height=15)
        self.texto.pack(padx=10, pady=10)

        # Botón de análisis
        self.boton = tk.Button(root, text="Analizar", command=self.analizar)
        self.boton.pack(pady=5)

        # Marco para resultados
        self.marco_resultados = tk.Frame(root)
        self.marco_resultados.pack(padx=10, pady=10)

        # Cuadro de resultados léxicos
        self.resultado_lexico = scrolledtext.ScrolledText(self.marco_resultados, width=50, height=10, state='normal')
        self.resultado_lexico.grid(row=0, column=0, padx=5)
        self.resultado_lexico.insert(tk.END, "Resultado Léxico:\n")

        # Cuadro de resultados sintácticos
        self.resultado_sintactico = scrolledtext.ScrolledText(self.marco_resultados, width=50, height=10, state='normal')
        self.resultado_sintactico.grid(row=0, column=1, padx=5)
        self.resultado_sintactico.insert(tk.END, "Errores Sintácticos:\n")
        self.resultado_sintactico.tag_configure("invalido", foreground="red")

        # Inicializar analizadores
        self.analizador = AnalizadorLexico()
        self.sintactico = AnalizadorSintactico()

    def analizar(self):
        # Obtener líneas y enumerarlas en el área de texto
        lineas = self.texto.get("1.0", tk.END).strip().split('\n')
        texto_enumerado = ""
        for i, linea in enumerate(lineas, 1):
            texto_enumerado += f"{i}: {linea.strip()}\n"
        self.texto.delete("1.0", tk.END)
        self.texto.insert(tk.END, texto_enumerado)

        # Limpiar cuadros de resultados
        self.resultado_lexico.config(state='normal')
        self.resultado_lexico.delete("1.0", tk.END)
        self.resultado_lexico.insert(tk.END, "Resultado Léxico:\n")

        self.resultado_sintactico.config(state='normal')
        self.resultado_sintactico.delete("1.0", tk.END)
        self.resultado_sintactico.insert(tk.END, "Errores Sintácticos:\n")

        # Quitar los números de línea antes de analizar
        for i, linea in enumerate(lineas, 1):
            # Si la línea ya tiene formato 'n: contenido', quitamos el prefijo
            if ':' in linea:
                linea = linea.split(':', 1)[1].strip()

            # Análisis léxico
            resultado_tokens = self.analizador.analizar(linea)[0][2]
            self.resultado_lexico.insert(tk.END, f"Línea {i}: {resultado_tokens}\n")

            # Análisis sintáctico solo para inválidos
            es_valido, error = self.sintactico.es_valida(linea)
            if not es_valido:
                mensaje = f"Línea {i}: Inválida. {error}\n"
                self.resultado_sintactico.insert(tk.END, mensaje, "invalido")

        self.resultado_lexico.config(state='disabled')
        self.resultado_sintactico.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
