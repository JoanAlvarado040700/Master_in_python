#Capturar y manejar errores en codigos


try:
    nombre = input("Cuale es tu nombre: ")

    if len(nombre) > 1:
        usuario = "Su nombre es: " +nombre
    print(usuario) 
except:
    print("Ha ocurrido un error, ingresa bien tu nombre: ")
else:
    print("Todo va bien!!!")
finally:
    print("Fin de la iteracion")
