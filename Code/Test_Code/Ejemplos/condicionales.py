name = "Fernando"

if (
    len(name) < 5
):  # Si el nombre tiene menos de 5 letras imprime "Mi nombre es corto"
    print("Mi nombre es corto")
elif (
    len(name) == 5
):  # Si el nombre tiene 5 letras imprime "Mi nombre no es corto ni largo"
    print("Mi nombre no es corto ni largo")
else:  # Si el nombre tiene más de 5 letras imprime "Mi nombre es largo"
    print("Mi nombre es largo")
