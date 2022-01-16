
ini = int(input("ingrese el numero inicial "))
fin = int(input("Ingrese el numero final"))

if ini < fin :
    for ini in range(ini,(fin +1)):
        print(ini)
else:
    for fin in range(fin,(ini + 1)):
        print(fin)
