"""Guardar información de personas:
- Nombre (str)
- Fecha de Nacimiento (dict[str, int])
- Teléfono (int)
- Nacionalidad (str)
"""

nombre = "Fausto"
fecha_nacimiento = {"dia": 31, "mes": 5, "año": 2003}
telefono = 5512345678
nacionalidad = "Mexicano"

nombre_2 = "Eduardo"
fecha_nacimiento_2 = {"dia": 7, "mes": 4, "año": 2010}
telefono_2 = 5587654321
nacionalidad_2 = "Mexicano"


class Persona:
    def __init__(self, nombre, fecha_nacimiento, telefono, nacionalidad):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.nacionalidad = nacionalidad

    def saludar(self):
        print("Hola, soy", self.nombre, "! Bienvenid@!")

    def calcular_edad(self):
        CURR_YEAR = 2024
        edad = CURR_YEAR - self.fecha_nacimiento["año"]
        print("Tengo", edad, "años!")


persona = Persona(nombre, fecha_nacimiento, telefono, nacionalidad)
persona_2 = Persona(nombre_2, fecha_nacimiento_2, telefono_2, nacionalidad_2)

persona.saludar()
persona.calcular_edad()
persona_2.saludar()
persona_2.calcular_edad()


class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print(self.nombre, "dice: WUF!")


perro = Perro("firulais")
perro.ladrar()


def bienvenida(algo):
    print("Bienvenido,", algo.nombre, "!")


bienvenida(persona)
bienvenida(persona_2)
bienvenida(perro)
saludar(perro)
