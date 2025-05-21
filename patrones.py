"""
Módulo que contiene todos los patrones válidos para el analizador léxico
"""

VALID_PATTERNS = [
    r"b1\.base\(\d+\)",
    r"b1\.cuerpo\(\d+\)",
    r"b1\.garra\(\d+\)",
    r"b1\.velocidad\(\d+\)",
    r"b1\.cerrarGarra\(\)",
    r"b1\.abrirGarra\(\)",
    r"b1\.repetir\(\d+\)",
    r"Robot r1",
    r"r1\.iniciar",
    r"r1\.velocidad=\d+",
    r"r1\.base=\d+",
    r"r1\.cuerpo=\d+",
    r"r1\.garra=\d+",

    # Nuevos patrones para palabras genéricas y números
    r"[a-zA-Z_][a-zA-Z0-9_]*",  # Palabras (letras y números, pero no números al principio)
    r"\b\d+\b",                 # Números enteros
    r"\b\d+\.\d+\b",            # Números decimales
]
