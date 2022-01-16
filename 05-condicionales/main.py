# Condicional IF 

# Ejemplo 1
 
print("")
print("************ EJEMPLO 1   ***********")

print("Bienvenido !, por favor ingrese sus datos ")

usuario = "Joan"
verificacion = input("por favor ingrese sus nombre de usuario")
if usuario == verificacion:
    print(f"Sea Bienvenido joven {usuario} ")
else:
    error = "Sus datos no son correctos "
    print(error)

