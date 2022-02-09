def menu():
    print("============== Menu principal =========")
    print("""
    
    1-> listar cursos
    2-> Registrar curso
    3-> Actualizar lista 
    4-> Eliminar curso
    5-> Salir 

    ===============
    
    """)
opc = int(input("Seleccione una opcion..."))

if opc < 5 or opc > 5:
    print("Opcion incorrecta, intente nuevamente")
elif opc == 5:
    print("Gracias por usar este sistema")
else:
    ejecutarOpc(opc)

def ejecutarOpc(opc):
    print(opc)


menu()

