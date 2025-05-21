
import re

# Patrones válidos de sintaxis completa
SINTAXIS_VALIDAS = [
    r"b1\.base\(\d+\)",          # b1.base(10)
    r"b1\.cuerpo\(\d+\)",        # b1.cuerpo(10)
    r"b1\.garra\(\d+\)",         # b1.garra(10)
    r"b1\.velocidad\(\d+\)",     # b1.velocidad(10)
    r"b1\.cerrarGarra\(\)",      # b1.cerrarGarra()
    r"b1\.abrirGarra\(\)",       # b1.abrirGarra()
    r"b1\.repetir\(\d+\)",       # b1.repetir(10)
    r"Robot r1",                 # Robot r1
    r"r1\.iniciar",              # r1.iniciar
    r"r1\.velocidad=\d+",        # r1.velocidad=10
    r"r1\.base=\d+",             # r1.base=10
    r"r1\.cuerpo=\d+",           # r1.cuerpo=10
    r"r1\.garra=\d+"             # r1.garra=10
]

class AnalizadorSintactico:
    def __init__(self):
        self.sintaxis = [re.compile(p) for p in SINTAXIS_VALIDAS]

    def es_valida(self, linea):
        # Revisar qué patrón coincide con la línea
        for patron in self.sintaxis:
            match = patron.fullmatch(linea.strip())
            if match:
                return True, ""  # Sintaxis válida
        # Si no coincide con ningún patrón, es inválido
        return False, self.obtener_error(linea)

    def obtener_error(self, linea):
        # Revisión de errores específicos en la línea
        if re.search(r"[^a-zA-Z0-9_\.\(\) ]", linea):  # Detecta caracteres no permitidos
            return "Error: Contiene caracteres no permitidos (mayúsculas incorrectas, puntos, etc.)."
        
        # Error específico de paréntesis
        if re.search(r"\(\)", linea):  # Detecta paréntesis vacíos
            return "Error: Paréntesis vacíos en el comando."

        # Verificar que el uso de mayúsculas esté permitido
        if re.search(r"b1\.[A-Z]", linea):  # b1. seguido de mayúsculas
            return "Error: Las letras después de 'b1.' deben ser minúsculas."
        
        # Verificar el uso incorrecto de mayúsculas en 'Robot r1'
        if "Robot" in linea and "r1" in linea:
            return "Error: 'Robot' debe ir en minúsculas, debe ser 'robot r1'."

        # Validar si el formato de un número está mal
        if re.search(r"\d+[a-zA-Z]", linea):  # Si aparece un número seguido de una letra
            return "Error: Formato incorrecto, se esperaba un número entero o flotante."

        return "Error: Sintaxis desconocida. Verifica la estructura de la línea."
