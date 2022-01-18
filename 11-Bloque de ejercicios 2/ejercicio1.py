'''

Hacer una lista que tenga 8 numeros 8 numeros enteros y haga lo siguente:
1- Recorrer la lista y mostrarla 
2- Ordenarla y mostrar 
3- Buscar algun elemento ( Que el usuario pida por teclado)

'''

numeros = []

for n in range(1,9):
    valor = int(input("Ingrese un valor: "))
    numeros.append(valor)

def mostrar():
    for numero in numeros:
        print(numero)
opc = None
while opc != 0:
    print("\nLista de opciones: \n 1-> Recorrer la lista y mostrarla \n 2-> Ordenar y mostrar lista \n 3- Buscar algun elemento que el usuario pida \n4-> Mostrar la longitud \n 0-> Para finaliza")
    opc = int(input("Ingrese una ipcion: "))
    if opc == 1:
        mostrar()
    elif opc == 2:
        print(f"\nLista original: {numeros} ")
        numeros.sort()
        print(f"Numeros ordenados: {numeros} ")
    elif opc == 3:
        busqueda = int(input("\nIngrese lo que desea buscar:"))
        print(busqueda in numeros)
    elif opc == 4:
        print(f"La cantidad de datos es: {len(numeros)}")
        
    elif opc == 0:
        print("Muchas gracias")
        

    else:
        print("Revise las opciones")