'''
Pedir dos numeros al usuario y hacer y hacer todas las 
operaciones basicas de una calculadora

'''
print("MINI CALCULADORA")

valor1 = int(input("ingrese el primer valor "))
valor2 = int(input("Ingrese el segundo valor "))

print("Seleccione una opcion: ")
print("1 = Sumar")
print("2 = resta")
print("3= Multiplicacion")
print("4= Divicion")
print("----------------------------------------------")
opc = int(input("Ingrese una opcion"))

if opc == 1:
    resul = valor1 +valor2
    print(f"El resultado de la suma es: {resul} " )
elif opc == 2:
    resul = valor1  - valor2
    print(f"El resultado de la resta es: {resul} " )
elif opc == 3:
    resul = valor1  * valor2
    print(f"El resultado de la multiplicacion es: {resul} " )
elif opc == 4:
    resul = valor1  / valor2
    print(f"El resultado de la resta es: {resul} " )
else:
    print("Invalid option")
