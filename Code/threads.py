"""Implementación paralela del lexer

Este archivo contiene la implementación paralela del lexer. Está diseñado para
correrse como un script que analice los archivos .py contenidos dentro de un
cierto PATH dado al script.

Alternativamente, se puede utilizar como módulo y llamarse desde un script
externo.
"""

import os
import time
from concurrent.futures import ProcessPoolExecutor
from lexer import lexer

def parse_file(path):
    """Resaltar un archivo produciendo un .html que contenga el formato."""
    with open(f"{path.removesuffix('.py')}.html", "w") as f2:
        f2.write(lexer(path))

def get_py_files(path):
    """Recursivamente navegar el path y recolectar todos los archivos .py"""
    py_files = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))
    return py_files

def main():
    path = os.path.join(os.getcwd(), "Test_Code")

    # Obtener todos los archivos .py
    py_files = get_py_files(path)

    # Definir el número de procesos a usar
    num_processes = min(2, os.cpu_count() or 1)  # Usar al menos 1 proceso, máximo 4 o el número de núcleos disponibles

    ti = time.perf_counter()

    # Usar ProcessPoolExecutor para procesar archivos en paralelo
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        executor.map(parse_file, py_files)

    tf = time.perf_counter()
    print(f"Time elapsed: {tf - ti} seconds")

if __name__ == "__main__":
    main()

