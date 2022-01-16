'''
Muestra todos los numeros impares que se encuentren entre dos numeros que ingrese el usuario
'''

total = 0
ini = int(input("Ingrese el numero inicial: "))
fin = int(input("Ingrese el segundo numero: "))

if ini < fin:
    for ini in range(ini,fin):
        if ini %2 != 0:
            print(ini)
            total += 1
else: 
    for fin in range(fin,ini):
        if fin %2 != 0:
            print(fin)
            total += 1

print(f"El tolal de numeros impares es: {total}  ")