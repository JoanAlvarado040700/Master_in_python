''''
Un programa que nos permita conseguir el porcentaje de un numero 
ingresado por el usuario 

'''''

valor = int(input("Ingrese una cantidad: "))
print(f"El valor ingresado es de: {valor}")

porcen = int(input("Que porcentaje desea obtener ?? "))

total = (porcen/100) * valor

print(f"El {porcen}% de {valor} es: {total} ")