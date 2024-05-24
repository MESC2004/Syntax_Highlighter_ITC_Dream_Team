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
    nums = "0123456789"
    letras = "abcdfghijklmnopqrstuvwxyzABCDFGHIJKLMNOPQRSTUVWXYZ"
    blank = " \t$"

    while (file[index] != "$" or (file[index] == "$" and estado != 0)) and (
        estado != 21
    ):
        char = file[index]
        if char in nums:
            col = 0
        elif char == "+":
            col = 1
        elif char == "-":
            col = 2
        elif char == "*":
            col = 3
        elif char == "/":
            col = 4
        elif char == "^":
            col = 5
        elif char == "=":
            col = 6
        elif char == ".":
            col = 7
        elif char in letras:
            col = 8
        elif char == "(":
            col = 9
        elif char == ")":
            col = 10
        elif char in "eE":
            col = 11
        elif char in "\n$":
            col = 12
        elif char in blank:
            col = 13
        else:
            col = 14

        estado = tabla[estado][col]
        if estado == 9:
            print(lexema + " INT")
            estado = 0
            lexema = ""
            index -= 1
        elif estado == 10:
            print(lexema + " REAL")
            estado = 0
            lexema = ""
            index -= 1
        elif estado == 11:
            print("+" + " SUMA")
            estado = 0
            lexema = ""
        elif estado == 12:
            print("-" + " RESTA")
            estado = 0
            lexema = ""
        elif estado == 13:
            print("*" + " MULTIPLICACION")
            estado = 0
            lexema = ""
        elif estado == 14:
            print("(" + " PARENTESIS ABRE")
            estado = 0
            lexema = ""
        elif estado == 15:
            print(")" + " PARENTESIS CIERRA")
            estado = 0
            lexema = ""
        elif estado == 16:
            print(lexema + " VARIABLE")
            estado = 0
            lexema = ""
            index -= 1
        elif estado == 17:
            print(lexema + " COMENTARIO")
            estado = 0
            lexema = ""
        elif estado == 18:
            print("/" + " DIVISION")
            estado = 0
            lexema = ""
            index -= 1
        elif estado == 19:
            print("^" + " POTENCIA")
            estado = 0
            lexema = ""
        elif estado == 20:
            print("=" + " ASIGNACION")
            estado = 0
            lexema = ""
        elif estado == 21:
            print("ERROR")

        index += 1

        if estado != 0:
            lexema += char
