#Usar parametros en una funcion
'''
nombre = input("Ingrese su nombre")
def datos(nombre):
    print(f"Su nombre es: {nombre} ")

datos(nombre)
'''



# Ejemplo: Tablas de multiplicar 


def tabla(numero):
    print(f" Tabla de miltiplicar del {numero} ")
    for n in range( 11):
        print(f" {numero} * {n} = {numero * n} ")
    print("--------------------------------------------------")


for num in range(1,11):
    tabla(num)