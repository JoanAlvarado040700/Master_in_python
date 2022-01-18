'''

Crear u  scrip que tenga 4 variables: lista, string, entero y booleano
y que imprima un mensaje segun el tipo de dato de cada variable. 
-> Usar funciones

'''

def comprobar(dato,type):
    test = isinstance(dato,type)
    result = ""
    if test:
        result = f"EL tipo de dato es: {type(dato)} "
    else:
        result = "Dato no correspondido"
    return result



lista = ["Joan",21,"pamela",20]
cadena = "Hola que tal"
num = 21
si = True

print(comprobar(lista,list))




