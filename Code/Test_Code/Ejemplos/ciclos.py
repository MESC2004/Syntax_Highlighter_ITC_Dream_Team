# Repetición de código dependiendo ciertas condiciones.
# for-loops: se repiten por un número determinado de veces

# Calcular un promedio utilizando for-loops
calificaciones = [7, 9, 10, 8, 6, 5, 6, 8, 0, 2, 5, 4]

suma = 0
print(suma)
for calificacion in calificaciones:
    suma += calificacion
    print(suma)

promedio = suma / len(calificaciones)

print("El promedio de las calificaciones", calificaciones, "es:", promedio)

# Imprimir un nombre por renglones letra por letra
nombre = "FAUSTO"
letras = ["F", "A", "U", "S", "T", "O"]

for letra in letras:
    print(letra)

for letra in nombre:
    print(letra)

# while-loops: se repiten mientras una condición sea cierta

age = int(input("Introduce tu edad: "))
faltantes = 0
while age < 18:
    print("En", faltantes, "años, seguirás siendo menor de edad")
    age += 1
    faltantes += 1

print("Te faltan", faltantes, "años para ser mayor de edad")

# Calcular el promedio usando while-loops
calificaciones = [7, 9, 10, 8, 6, 5, 6, 8, 0, 2, 5, 4, 3, 8, 10, 9]

suma = 0
indice = 0
while indice >= 0 and indice <= len(calificaciones) - 1:
    suma += calificaciones[indice]
    indice += 1

promedio = suma / len(calificaciones)

print("El promedio de las calificaciones", calificaciones, "es:", promedio)
