# Funciones dentro de otras funciones
from cgitb import text


def getNombre(nombre):
    texto = f"Su nombre es: {nombre} "
    return texto
def getApellido(apellido):
    texto = f"Su apellido es: {apellido} "
    return texto

def datos(nombre,apellido):
    texto = getNombre(nombre) + "\n" + getApellido(apellido)
    return texto

print(datos("Joan","Larios"))
