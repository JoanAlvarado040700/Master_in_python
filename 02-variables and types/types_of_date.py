#------------------- Tipos de datos 
nada = None # Vacio
n1 = 'Joan'
n2 = 21     # int
n3 = 10.4   # float
n4 = True   # Boleano
lista = [19,2,4]
tupla = ("tengo 21 años")  # Son variables estaticas
diccionario = {
    "Nombre" : "Joan ",
    "Apellido" : "Larios",
    "Novia" : "pamela"
}

rango = range(10, 5, 50)
# ------------------------------------------------
print (lista)
print(type(lista))

print("----------------------------------------------------")

'''En python no se necesita definir el tipo de dato, no obstante esto
puede ser un problema cuando usamos la misma variable y le añadimos otrio 
tipo de dato'''
# ------------>> Concatenar 

print(f"Hola mi nombre es {n1} ")

print("mi edad es de {} ".format(n2))

# ------------------>>>> Trasnformar un dato 

n2 = str(23)

