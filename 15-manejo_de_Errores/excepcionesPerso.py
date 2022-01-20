#Excepciones personalizadas o lanzar excepciones

nombre = input("Introduce el nombre")
edad = int(input("introduce la edad"))

if edad < 5 or edad > 110:
    raise ValueError ("La edad introducida no es real")
elif len(nombre) <= 1:
    raise ValueError("El nombre no esta completo")
else:
    print("Bienvenido al master en python")
