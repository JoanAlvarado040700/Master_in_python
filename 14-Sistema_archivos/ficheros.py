from io import open
import pathlib
from posixpath import abspath

#Abrir un archivo

ruta = str(pathlib.Path().absolute()) +"/14-Sistema_archivos/ejemplo.txt"
print(ruta)

archivo = open(ruta,"a+")

#Escribir dentro de un archivo

archivo.write("******** Soy un texto metido desde python*********** \n")

#cerrar archivo

archivo.close()

#Leer contenido

ruta = str(pathlib.Path().absolute()) +"/14-Sistema_archivos/ejemplo.txt"
print(ruta)

archivo2 = open(ruta,"r")
#contenido = archivo2.read()
#print(contenido)

#leer contenido y guardarlo en lista


lista = archivo2.readlines()
archivo2.close()

for elementos in lista:
    print("-> "+elementos.upper())

#Copiar un archivo 

import shutil
'''

ruta_original = str(pathlib.Path().absolute()) +"/14-Sistema_archivos/ejemplo.txt"
ruta_nueva = str(pathlib.Path().absolute()) +"/14-Sistema_archivos/ejemplo_copiado.txt"

shutil.copyfile(ruta_original,ruta_nueva)

'''


#Mover y renombrar un archivo
'''
ruta_original = str(pathlib.Path().absolute()) +"/14-Sistema_archivos/ejemplo.txt"
ruta_nueva = str(pathlib.Path().absolute()) +"/14-Sistema_archivos/ejemplo_copiado_nuevo.txt"

shutil.move(ruta_original,ruta_nueva)

'''

#Eliminar un archivo

import os
'''
ruta_nueva = str(pathlib.Path().absolute()) +"/14-Sistema_archivos/ejemplo_copiado.txt"
os.remove(ruta_nueva)
'''


#Comprobar si un archivo existe

import os.path

#print(os.path.abspath("../"))

#Crear carpetas:

if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya existe la carpeta")

#------------->liminar carpeta

#os.rmdir("./mi_carpeta")
