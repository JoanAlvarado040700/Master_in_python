'''
Proyecto python y Mysql:

-> Abrir asistente
-> Login o registro
-> Si elegimos registrarnos, nos creara un usuario en la bs
-> si elegimos login, identificara al usuario y nos preguntara 
-> crear nota, mostrar notas y borrarlas 

'''
from Usuarios import acciones

print(""" Acciones disponibles: 

    -> Registro
    -> Login

""")

realizar = acciones.Acciones()


accion = input("Que desea realizar? ")

if accion == "registro": 
    realizar.registro()

elif accion == "login":
    realizar.login()
