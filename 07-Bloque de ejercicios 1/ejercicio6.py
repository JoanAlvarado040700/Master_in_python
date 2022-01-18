'''
Mostrar las tablas de multiplicacion del 1 al 10

'''

for n in range(0,11):
    print("------------------------------")
    print(f"Tabla de multiplicar del {n} ")
    for j in range(0,11):
        resul = n * j
        print(f" {n} * {j} = {resul} ")
    print("")