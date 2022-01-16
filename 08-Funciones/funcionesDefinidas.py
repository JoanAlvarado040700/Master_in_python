#Funciones predefinidas en python 

from cgitb import text


nombre = "Joan Larios"
#Funciones generales

print(type(nombre))

#Detectar el tipado

comprobar = isinstance(nombre,str)
if comprobar: print("Es una cadena de caracteres")
else: print(" Non es una cadena de caracteres")

#Limpiar espacios 

if not isinstance(nombre,float):
    frace = "           Esto no es un flotante            "
    print(frace.strip())

#Eliminar variables

year = 2022

print(year)
del year

#Comprobar variables vacias 

texto = "Larga vida al rey XD"
if len(texto) <= 0: print("La variable esta vacia")
else: print("La variable cuenta con: ",len(texto), "caracteres" )

#Encontrar caracteres

print(texto.find("vida"))

#Reemplazo de de palabras

nueva = texto.replace("Larga", "Corta")
print(nueva)

#Cambio de mayusculas

print(texto.upper())
