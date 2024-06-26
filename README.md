# Resaltador de sintaxis

## Equipo

- Fausto Jiménez de la Cuesta Vallejo A01027983
- Miguel Enrique Soria A01028033
- José Antonio González Martínez A01028517

## Descripción de la evidencia 1

1. Selecciona un lenguaje de programación que te resulte familiar, y determina 
    las categorías léxicas que tienen en común (por ejemplo, palabras 
    reservadas, operadores, identificadores, comentarios, etc.).
2. Usando Python implementa un resaltador léxico que logre escanear los 
    elementos léxicos de cualquier archivo fuente provisto.
3. El programa debe convertir su entrada en documentos de HTML+CSS que 
    resalten su léxico con diferentes colores de acuerdo al tipo de token (por 
    ejemplo, palabras reservadas, operadores, identificadores, comentarios, 
    etc.).
4. Utiliza las convenciones de codificación del lenguaje en el que está 
    implementado tu programa.
5. Reflexiona sobre la solución planteada, los algoritmos implementados y 
    sobre el tiempo de ejecución de estos.
6. Calcula la complejidad de tu algoritmo basada en el número de iteraciones y 
    contrástala con el tiempo obtenido en el punto 5 para ver si son parecidos.
7. Plasma en un breve reporte de una página las conclusiones de tu reflexión 
    en los puntos 7 y 8. Agrega además una breve reflexión sobre las 
    implicaciones éticas que el tipo de tecnología que desarrollaste pudiera 
    tener en la sociedad.

## Lexemas y Colores

- **Delimiters** (![#6C7D9C](https://placehold.co/15x15/6C7D9C/6C7D9C.png)`#6c7d9c`):
    - `[`
    - `]`
    - `(`
    - `)`
    - `{`
    - `}`

- Operators (![#C75AE8](https://placehold.co/15x15/C75AE8/C75AE8.png)`#C75AE8`):
    - `+`
    - `-`
    - `*`
    - `/`
    - `^`
    - `=`
    - `<`
    - `>`
    - `%`
    - `!=`
    - `;`
    - `and`
    - `or`
    - `not`

- Reserved Words and keys (![#C75AE8](https://placehold.co/15x15/C75AE8/C75AE8.png)`#C75AE8`):
    - `:`
    - `if`
    - `else`
    - `elif`
    - `for`
    - `while`
    - `with`
    - `as`
    - `def`
    - `in`
    - `class`
    - `import`
    - `range`
    - `print`
      
- Datatypes (![#EFBD5D](https://placehold.co/15x15/EFBD5D/EFBD5D.png)`#EFBD5D`):
    - `int`
    - `float`
    - `complex`
    - `str`
    - `list`
    - `tuple`
    - `range`
    - `dict`
    - `set`
    - `frozenset`
    - `bool`
    - `bytes`
    - `bytearray`
    - `memoryview`
    

- Variables and function calls (![#F65866](https://placehold.co/15x15/F65866/F65866.png)`#F65866`)
    - Variable declarations (asvsdv y un =)
    - functname(lo de aqui sigue los colores del highlighter dependiendo de lo que sea)

- Strings (![#8BCD5B](https://placehold.co/15x15/8BCD5B/8BCD5B.png)`#8BCD5B`)
    - `"..."`
    - `'...'`

- Comments (![#34BFD0](https://placehold.co/15x15/34BFD0/34BFD0.png)`#34BFD0`)
    - `#` until return

- Multiline Comments (![#34BFD0](https://placehold.co/15x15/34BFD0/34BFD0.png)`#34BFD0`)
    - `""" ... """`
- Integers and Real Numbers (![#DD9046](https://placehold.co/15x15/DD9046/DD9046.png)`#DD9046`)
    - All with digits and followed by point
