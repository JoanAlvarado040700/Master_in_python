'''
Escribir un script que muestre los numeros pares del 1 al 120 
'''
n = 1

for n in range(1,121):
    if(n %2 == 0 ):
        print(n)
    n+=1
