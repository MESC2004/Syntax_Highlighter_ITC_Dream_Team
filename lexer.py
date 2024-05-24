import re

# Tabla de estados y de inputs
tabla = [
    [1, 11, 12, 13, 4, 19, 20, 8, 3, 14, 15, 3, 0, 0, 21],
    [1, 9, 9, 9, 9, 9, 9, 2, 21, 9, 9, 21, 9, 9, 21],
    [2, 10, 10, 10, 10, 10, 10, 21, 21, 10, 10, 6, 10, 10, 21],
    [3, 16, 16, 16, 16, 16, 16, 21, 3, 16, 16, 3, 16, 16, 21],
    [18, 18, 18, 18, 5, 18, 18, 18, 18, 18, 18, 18, 18, 18, 21],
    [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 17, 5, 5],
    [6, 21, 7, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
    [2, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
    [2, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
]


def lexer(filename: str):
    """
    :param filename: string representando el path relativo al archivo .py a
        leer.
    :return: string
    """
    with open(filename, "r") as f:
        file = f.read()

    lexema = ""
    estado = 0
    columna = 0
    index = 0
    html = ""

    while (file[index] != "$" or (file[index] == "$" and estado != 0)) and (
        estado != 21
    ):
        char = file[index]
        if char == "+":
            col = 1
        elif char == "-":
            col = 2
        elif char == "*":
            col = 3
        elif char == "/":
            col = 4
        elif char == "^":
            col = 5
        elif char == "(":
            col = 9
        elif char == ")":
            col = 10
        elif char == "=":
            col = 6
        elif char == ".":
            col = 7
        elif re.match(r"e|E", char):
            col = 11
        elif re.match(r"\d", char):
            col = 0
        elif re.match(r"\w", char):
            col = 8
        elif re.match(r"\n|$", char):
            col = 12
        elif re.match(r"\s", char):
            col = 13
        else:
            col = 14

        estado = tabla[estado][col]
        if estado == 9:
            print(lexema + " INT")
            html += '<font color="red">' + lexema + "</font>"
            estado = 0
            lexema = ""
            index -= 1
        elif estado == 10:
            print(lexema + " REAL")
            html += '<font color="blue">' + lexema + "</font>"
            estado = 0
            lexema = ""
            index -= 1
        elif estado == 11:
            print("+" + " SUMA")
            html += '<font color="purple">' + "+" + "</font>"
            estado = 0
            lexema = ""
        elif estado == 12:
            print("-" + " RESTA")
            html += '<font color="purple">' + "-" + "</font>"
            estado = 0
            lexema = ""
        elif estado == 13:
            print("*" + " MULTIPLICACION")
            html += '<font color="purple">' + "*" + "</font>"
            estado = 0
            lexema = ""
        elif estado == 14:
            print("(" + " PARENTESIS ABRE")
            html += '<font color="purple">' + "(" + "</font>"
            estado = 0
            lexema = ""
        elif estado == 15:
            print(")" + " PARENTESIS CIERRA")
            html += '<font color="purple">' + ")" + "</font>"
            estado = 0
            lexema = ""
        elif estado == 16:
            print(lexema + " VARIABLE")
            html += '<font color="orange">' + lexema + "</font>"
            estado = 0
            lexema = ""
            index -= 1
        elif estado == 17:
            print(lexema + " COMENTARIO")
            html += '<font color="brown">' + lexema + "</font>"
            estado = 0
            lexema = ""
        elif estado == 18:
            print("/" + " DIVISION")
            html += '<font color="purple">' + "/" + "</font>"
            estado = 0
            lexema = ""
            index -= 1
        elif estado == 19:
            print("^" + " POTENCIA")
            html += '<font color="purple">' + "^" + "</font>"
            estado = 0
            lexema = ""
        elif estado == 20:
            print("=" + " ASIGNACION")
            html += '<font color="purple">' + "=" + "</font>"
            estado = 0
            lexema = ""
        elif estado == 21:
            print("ERROR")

        index += 1

        if estado != 0:
            lexema += char

    return html


def main():
    with open("lexer.html", "w") as html:
        html.write(lexer("lexer.py"))


if __name__ == "__main__":
    main()
