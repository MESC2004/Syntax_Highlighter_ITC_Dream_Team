"""Definición del comportamiento del Lexer.

Éste está destinado a ser un módulo importado por otros módulos. No se ejecuta
de forma independiente.

Este archivo está destinado a tener toda la definición y el comportamiento de
DFA por medio de la TABLA de estados para el lexer, así como la función que se
encarga de analizar un archivo y producir su versión resaltada en un archivo
.html.
"""

import re

# Tabla de estados y de inputs
TABLA = [
    [1, 10, 5, 14, 16, 7, 8, 6, 5, 9, 9, 19],
    [1, 2, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11],
    [2, 19, 19, 12, 12, 19, 19, 19, 3, 12, 12, 19],
    [4, 19, 19, 4, 19, 19, 19, 19, 19, 19, 19, 19],
    [4, 19, 19, 12, 19, 19, 19, 19, 19, 12, 12, 19],
    [5, 5, 5, 13, 13, 13, 13, 19, 13, 13, 13, 19],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 15, 6, 6],
    [7, 7, 7, 7, 7, 17, 7, 7, 7, 19, 7, 7],
    [8, 8, 8, 8, 8, 8, 17, 8, 8, 19, 8, 8],
    [18, 18, 18, 18, 18, 18, 18, 18, 18, 9, 9, 18],
    [2, 19, 19, 19, 19, 19, 19, 19, 1, 19, 19, 19],
]
PALABRAS_RESERVADAS = [
    "if",
    "else",
    "elif",
    "while",
    "for",
    "in",
    "range",
    "print",
    "def",
    "return",
    "True",
    "False",
    "None",
    "and",
    "or",
    "not",
    "break",
    "continue",
    "class",
    "is",
    "try",
    "except",
    "finally",
    "raise",
    "import",
    "from",
    "as",
    "with",
    "yield",
    "assert",
    "del",
    "global",
    "lambda",
    "nonlocal",
    "pass",
    "async",
    "await",
    "int",
    "float",
    "str",
    "bool",
    "list",
    "dict",
    "set",
    "filename",
]
OPERADORES = ["+", "-", "*", "/", "^", "="]
ESPECIALES = [
    "(",
    ")",
    "{",
    "}",
    "[",
    "]",
    ",",
    ";",
    ":",
    "@",
    "%",
    "&",
    "|",
    "!",
    "?",
    "<",
    ">",
]


def lexer(filename: str):
    """Producir .html con resaltado de syntax de un archivo .py

    Leer el archivo en una variable como un string, y posteriormente leer el
    string un caracter a la vez. Utilizando la TABLA de estados, identificar
    los tokens contenidos en el archivo .py y añadirlos al .html generado con
    el resalte correspondiente.
    """
    with open(filename, "r") as f:
        file = f.read()

    lexema = ""
    estado = 0
    columna = 0
    index = 0
    html = ""

    while (index < len(file) or (index < len(file) and estado != 0)) and (
        estado != 19
    ):
        char = file[index]
        if re.match(r"\d", char):
            col = 0
        elif char == ".":
            col = 1
        elif re.match(r"e|E", char):
            col = 8
        elif re.match(r"\w", char):
            col = 2
        elif char in operadores:
            col = 3
        elif char in especiales:
            col = 4
        elif char == "'":
            col = 5
        elif char == '"':
            col = 6
        elif char == "#":
            col = 7
        elif re.match(r"\n", char):
            # html+= "<br>"
            col = 9
        elif re.match(r"\t| ", char):
            col = 10
        else:
            col = 11

        estado = tabla[estado][col]

        if estado == 9:
            if char == "\n":
                html += "<br>"

        elif estado == 11:
            print(lexema + " INT")
            html += '<font color="#DD9046">' + lexema + "</font>"
            estado = 0
            lexema = ""
            index -= 1

        elif estado == 12:
            print(lexema + " REAL")
            html += '<font color="#DD9046">' + lexema + "</font>"
            estado = 0
            lexema = ""
            index -= 1

        elif estado == 13:
            if lexema in Palabras_reservadas:
                print(lexema + " PALABRA RESERVADA")
                html += '<font color="#0AA9BA">' + lexema + "</font>"
            else:
                print(lexema + " VARIABLE")
                html += '<font color="#F65866">' + lexema + "</font>"
            index -= 1
            estado = 0
            lexema = ""

        elif estado == 14:
            lexema += char
            print(lexema + " Operador")

            html += '<font color="#C75AE8">' + lexema + "</font>"
            estado = 0
            lexema = ""

        elif estado == 15:
            print(lexema + " comentario")
            html += '<font color="#34BFD0">' + lexema + "</font>"
            estado = 0
            index -= 1
            lexema = ""

        elif estado == 16:
            print(lexema + " Especial")
            lexema += char
            html += '<font color="#6c7d9c">' + lexema + "</font>"
            estado = 0
            lexema = ""

        elif estado == 17:
            print(lexema + " String")
            lexema += char
            html += '<font color="#8BCD5B">' + lexema + "</font>"
            estado = 0
            lexema = ""

        elif estado == 18:
            print(lexema + " blank space")
            html += lexema
            estado = 0
            index -= 1
            lexema = ""

        elif estado == 19:
            print("error")

        index += 1

        if estado != 0:
            lexema += char

    return html


if __name__ == "__main__":
    print("This is meant to be a module. Not a script.")
