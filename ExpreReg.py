#importar libreria de expresiones regulares
import re

#sustituyendo enteros por "aaaa"

patron= (r'\d+') #patron para encontrar enteros
string="1234 hola 5678"
sus="aaaa"
print(re.sub(patron,sus,string))

#recibe un token y lo sustituye por un html en rojo
def sustituir(match):
    return '<font color="red">'+'aaaa'+'</font>'

b=re.sub(patron,sustituir,string)
print(b)
f2=open("colorear.html","w")
f2.write(b)
f2.close()