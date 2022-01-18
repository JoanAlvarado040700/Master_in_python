'''

Programa que comprueve si una variable esta vacia y 
si esta vacia, rellenarla con texto en minuscula y
mostrarlo en mayuscula
'''

from random import random


texto = input("please, enter a dato: ")

if len(texto) <= 0:
    texto = input("ingrese algo en minuscula: ")
    print(texto)
    print(texto.upper())
