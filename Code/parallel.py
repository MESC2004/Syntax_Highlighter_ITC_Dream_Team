"""Implementación paralela del lexer

Este archivo contiene la implementación paralela del lexer. Está diseñado para
correrse como un script que analice los archivos .py contenidos dentro de un
cierto PATH dado al script.

Alternativamente, se puede utilizar como módulo y llamarse desde un script
externo.
"""

import os
import time
import threading
from lexer import lexer


def get_files(path):
    """Recursivamente navegar el path y resaltar los archivos .py"""
    with os.scandir(path) as ficheros:
        for fichero in ficheros:
            if fichero.is_dir():
                get_files(os.path.join(path, fichero.name))

            elif fichero.is_file() and fichero.name.endswith(".py"):
                f2 = open(f"{fichero.name.removesuffix('.py')}.html", "w")
                f2.write(lexer(os.path.join(path, fichero.name)))
                f2.close()


def main():
    ti = time.perf_counter()
    get_files(os.path.join(os.getcwd(), "Test_Code"))
    tf = time.perf_counter()
    print(f"Time elapsed: {tf-ti} seconds")


if __name__ == "__main__":
    main()