import re
from patrones import VALID_PATTERNS

# Clasificación de los tipos de tokens
TOKEN_TYPES = {
    'identificador': r"[a-zA-Z_][a-zA-Z0-9_]*",
    'numero': r"\b\d+\b|\b\d+\.\d+\b",  # Incluye enteros y decimales
}

class AnalizadorLexico:
    def __init__(self):
        self.patterns = [re.compile(p) for p in VALID_PATTERNS]

    def analizar(self, texto):
        lineas = texto.strip().split('\n')
        resultado = []

        for numero, linea in enumerate(lineas, 1):
            tokens_validos = []
            for patron in self.patterns:
                match = patron.finditer(linea)
                for m in match:
                    token = m.group()
                    tipo_token = self.obtener_tipo_token(token)
                    tokens_validos.append(f"{token} ({tipo_token})")
            
            if not tokens_validos:
                tokens_validos.append("(sin tokens reconocidos) Invalido")

            resultado.append((numero, linea, " ".join(tokens_validos)))

        return resultado

    def obtener_tipo_token(self, token):
        if re.match(TOKEN_TYPES['identificador'], token):
            return "Identificador"
        elif re.match(TOKEN_TYPES['numero'], token):
            return "Número"
        else:
            return "Símbolo"
