# Parametros opcionales 

def datos(nombre, dni = None):
    print("EMPLEADO:")
    print(f"El nombre del empleado es: {nombre} ")
    if dni != None:
        print(f"El DNI del usuario es: {dni} ")
