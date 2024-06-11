# Programa que pide un input al usuario de su año de nacimiento y
# regresa la edad del usuario de acuerda al año en el que nació.

# 1 - Recibir input año de nacimiento del usuario
# 2 - Convertir input año de nacimiento a int
birth_year = int(input("En qué año naciste? "))

# 3 - Hacer resta del año actual (2024) al año de nacimiento
# 4 - Imprimir mensaje con edad del usuario
CURRENT_YEAR = 2024

age = CURRENT_YEAR - birth_year

if age >= 0:
    print("Tienes " + str(age) + " años")
else:  # age < 0
    print("Pon tu fecha correcta de nacimiento")

# Es mayor a 18?
if age >= 18:
    print("Eres mayor de edad!")
# Es mayor o igual a 10?
elif age >= 10:
    print("Eres menor de edad!")
# Es mayor o igual a 0?
elif age >= 0:
    print("Tu edad aún tiene solo un dígito")
# Es menor a 0?
else:  # age < 0
    print("Felicidades! Todavía no naces!")
