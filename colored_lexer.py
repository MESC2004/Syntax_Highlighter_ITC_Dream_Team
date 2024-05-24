
# Miguel Soria A01028033
# 5/10/2024

"""Hacer un programa que reciba como entrada un archivo de texto que contenga 
expresiones aritméticas y comentarios, y nos regrese una tabla con cada uno de sus tokens encontrados, en el orden en que fueron encontrados e indicando de qué tipo son."""

# GUARDAR EL ARCHIVO EN LA MISMA CARPETA QUE EL PROGRAMA CON NOMBRE archivo.txt o el nombre deseado como string en el parametro FILENAME


tabla = [[1,	11,	12,	13,	4,	19,	20,	8,	3,	14,	15,	3,	0,	0,	21],
         [1,	9,	9,	9,	9,	9,	9,	2,	21,	9,	9,	21,	9,	9,	21],
         [2,	10,	10,	10,	10,	10,	10,	21,	21,	10,	10,	6,	10,	10,	21],
         [3,	16,	16,	16,	16,	16,	16,	21,	3,	16,	16,	3,	16,	16,	21],
         [18, 18, 18,18,	5,	18,	18,	18,	18,	18,	18,	18,	18,	18,	21],
         [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 17, 5, 5],
         [6, 21, 7, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
         [2, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
         [2, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21]]


def lexerAritmetico(filename):
    """
    :param filename: nombre del archivo, debe vivir dentro de la misma carpeta que el script
    :return: Regresa mediante prints los lexemas y sus tokens respectivos a partir del archivo de texto
    """
    with open(filename, 'r') as file:
        s = file.read()

    lexema = ""
    estado = 0
    columna = 0
    p = 0
    nums = "0123456789"
    letras = "abcdfghijklmnopqrstuvwxyzABCDFGHIJKLMNOPQRSTUVWXYZ"
    blank = " \t$"
    html=''
    

    while(s[p] != "$" or (s[p] == "$" and estado != 0)) and (estado != 21):
        c = s[p]
        if c in nums:
            col = 0
        elif c == "+":
            col = 1
        elif c == "-":
            col = 2
        elif c == "*":
            col = 3
        elif c == "/":
            col = 4
        elif c == "^":
            col = 5
        elif c == "=":
            col = 6
        elif c == ".":
            col = 7
        elif c in letras:
            col = 8
        elif c == "(":
            col = 9
        elif c == ")":
            col = 10
        elif c in "eE":
            col = 11
        elif c in "\n$":
            col = 12
        elif c in blank:
            col = 13
        else:
            col = 14

        estado = tabla[estado][col]
        if estado == 9:
            print(lexema +" INT")
            html+='<font color="red">'+lexema+'</font>'
            estado = 0
            lexema = ""
            p-=1
        elif estado == 10:
            print(lexema + " REAL")
            html+='<font color="blue">'+lexema+'</font>'
            estado = 0
            lexema = ""
            p-=1
        elif estado == 11:
            print("+" + " SUMA")
            html+='<font color="purple">'+'+'+'</font>'
            estado = 0
            lexema = ""
        elif estado == 12:
            print("-" + " RESTA")
            html+='<font color="purple">'+'-'+'</font>'
            estado = 0
            lexema = ""
        elif estado == 13:
            print("*" + " MULTIPLICACION")
            html+='<font color="purple">'+'*'+'</font>'
            estado = 0
            lexema = ""
        elif estado == 14:
            print("(" + " PARENTESIS ABRE")
            html+='<font color="purple">'+'('+'</font>'
            estado = 0
            lexema = ""
        elif estado == 15:
            print(")" + " PARENTESIS CIERRA")
            html+='<font color="purple">'+')'+'</font>'
            estado = 0
            lexema = ""
        elif estado == 16:
            print(lexema + " VARIABLE")
            html+='<font color="orange">'+lexema+'</font>'
            estado = 0
            lexema = ""
            p-=1
        elif estado == 17:
            print(lexema + " COMENTARIO")
            html+='<font color="brown">'+lexema+'</font>'

            estado = 0
            lexema = ""
        elif estado == 18:
            print("/" + " DIVISION")
            html+='<font color="purple">'+'/'+'</font>'
            estado = 0
            lexema = ""
            p-=1
        elif estado == 19:
            print("^" + " POTENCIA") 
            html+='<font color="purple">'+'^'+'</font>'

            estado = 0
            lexema = ""
        elif estado == 20:
            print("=" + " ASIGNACION")
            html+='<font color="purple">'+'='+'</font>'

            estado = 0
            lexema = ""
        elif estado == 21:
            print("ERROR")

        p+=1

        if estado != 0:
            lexema += c
            
    return html

lexerAritmetico("prueba.txt")
f2=open("colorear_test.html","w")
f2.write(lexerAritmetico("prueba.txt"))
f2.close()   
