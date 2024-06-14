"""Implementación paralela del lexer

Este archivo contiene la implementación paralela del lexer. Está diseñado para
correrse como un script que analice los archivos .py contenidos dentro de un
cierto PATH dado al script.

Alternativamente, se puede utilizar como módulo y llamarse desde un script
externo.
"""

import os
import time
from lexer import lexer
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime


def get_py_files(path):
    """Recursivamente navegar el path y recolectar todos los archivos .py"""
    py_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))
    return py_files


def process_file(file_path):
    """Procesar un solo archivo .py"""
    try:
        # debug
        # print(f"Processing {file_path} at {datetime.now().strftime('%H:%M:%S')}")
        with open(f"{file_path.removesuffix('.py')}.html", "w") as f2:
            f2.write(lexer(file_path))
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")


def main():
    path = os.path.join(os.getcwd(), "Test_Code")

    # Obtener todos los archivos .py
    py_files = get_py_files(path)

    # Definir el número de procesos a usar
    num_processes = min(4, os.cpu_count() or 1)  # Usar al menos 1 proceso, máximo 4 o el número de núcleos disponibles
    print(f"Using {num_processes} processes")

    ti = time.perf_counter()

    # Usar ProcessPoolExecutor para procesar archivos en paralelo
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        executor.map(process_file, py_files)

    tf = time.perf_counter()
    print(f"Time elapsed: {tf - ti} seconds")


if __name__ == "__main__":
    main()

