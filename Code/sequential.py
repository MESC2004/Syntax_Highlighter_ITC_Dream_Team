"""Implementación secuencial del lexer

Este archivo contiene la implementación secuencial del lexer. Está diseñado
para correrse como un script que analice los archivos .py contenidos dentro de
un cierto PATH dado al script.

Alternativamente, se puede utilizar como módulo y llamarse desde un script
externo.
"""
import os
import time
from lexer import lexer

ejemplo_dir = '/Users/jagle/OneDrive/Escritorio/Directorios/Syntax_Highlighter_ITC_Dream_Team/Code/Test_Code'
def get_files(path):
   
    with os.scandir(path) as ficheros:
        for fichero in ficheros:
            
            if (fichero.is_dir()):
                get_files(os.path.join(path, fichero.name))
                
            elif (fichero.is_file() and fichero.name.endswith('.py')):
                
                f2=open(f"{fichero.name}.html","w")
                f2.write(lexer(os.path.join(path, fichero.name)))
                f2.close()
                
if __name__=="__main__":
    ti=time.perf_counter()
    get_files(ejemplo_dir)
    tf=time.perf_counter()
    print(f"Time elapsed: {tf-ti} seconds")
    