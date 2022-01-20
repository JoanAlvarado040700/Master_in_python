from random import random
import crearModulos

print(crearModulos.hola("Joan"))


# Modulos de fechas:

import datetime

print(datetime.date.today())

fecha = datetime.datetime.now()

print(fecha)


#modulos de matematicas: 

import math

print("Raiz cuadrada de 10: ",math.sqrt(10))

print("numero pi: ", float(math.pi))

print("Redondear: ",  math.ceil(6.55574))


#Modulo random
import random
print("Numero aleatorio de 15 y 67: ", random.randint(15,67))