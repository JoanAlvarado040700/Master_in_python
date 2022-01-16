# Funciones y metodos para los arrays

Cantantes = ["bad bunny", "Julio iglecias", "mario", "mis vecinos"]

numeros = [1,2,14,5,6,7,12]


#ordenar 

print(numeros)
numeros.sort()
print(numeros)

#Añadir elementos 
print(Cantantes)
Cantantes.insert(2,"Panda")
print(Cantantes)

#Eliminar elementos

print( Cantantes)
Cantantes.pop(1)
print(Cantantes)
Cantantes.remove("bad bunny")
print(Cantantes)

#Dar la vuelta
numeros.reverse()
print(numeros)

#Buscar dentro de una lista
print("Panda" in Cantantes)

# Contan elementos

print(len(Cantantes))