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


def parse_file(path):
    """Resaltar un archivo produciendo un .html que contenga el formato."""
    with open(f"{path.removesuffix('.py')}.html", "w") as f2:
        f2.write(lexer(path))
        f2.close()


def get_files(path):
    """Recursivamente navegar el path y resaltar los archivos .py"""
    with os.scandir(path) as ficheros:
        hilos = []
        for fichero in ficheros:
            if fichero.is_dir():
                hilos.append(
                    threading.Thread(
                        name=f"get_files:{fichero}",
                        target=get_files,
                        args=(fichero.path,),
                    )
                )
                hilos[-1].start()

            elif fichero.is_file() and fichero.name.endswith(".py"):
                hilos.append(
                    threading.Thread(
                        name=f"parse_file:{fichero}",
                        target=parse_file,
                        args=(fichero.path,),
                    )
                )
                hilos[-1].start()

        for hilo in hilos:
            hilo.join()


def main():
    ti = time.perf_counter()
    get_files(os.path.join(os.getcwd(), "Test_Code"))
    tf = time.perf_counter()
    print(f"Time elapsed: {tf-ti} seconds")


if __name__ == "__main__":
    main()
