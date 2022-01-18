'''
Ingrese la cantidad de 15 notas y decir cuantos han aprovado 

'''

aprovados = 0
reprovados = 0
for n in range(1,16):
    notas = int(input("Ingrese una nota: "))
    if notas >= 60:
        aprovados += 1
    elif notas < 60:
        reprovados += 1
print("")
print(f" La cantidad de aprovados son: {aprovados} ")
print(f"La cantidad de reprovados es de:   {reprovados} ")
