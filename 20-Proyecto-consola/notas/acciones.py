import notas.notas as modelo


class accion():
    def crear(self, usuario):
        print(f"Ok {usuario[1]}!! vamos a generar una nueva nota  " )

        titulo = input("Introduce el titulo de una nuetu nota ")
        descripcion = input("Descripcion de la nota: ")

        nota = modelo.notes(usuario[0],titulo,descripcion)
        guardar = nota.save()

        if guardar[0] >= 1: print(f"Nota {nota.titulo} guardada de manera exitosa!! ")

        else: print("No se ha guardado la nota ")
    
    def mostrar(self, usuario):
        print(f"  ok {usuario[1]}!! aqui tienes tus notas:  ")

        nota = modelo.notes(usuario[0],'','')
        notas = nota.listar()
        for nota in notas:
            print("*****************************************************************")
            print("Titulo:        ",nota[2])
            print(nota[3])
            print("****************************************************************")

    def borrar(self, usuario):

        print(f"okey {usuario[1]}! vamos a borrar una nota ")

        titulo = input("introduce el titulo que desea eliminar: ")

        nota = modelo.notes(usuario[0],titulo,"")
        eliminar = nota.eliminar()

        if eliminar[0] >= 1: print(f"La nota se ha borrado con exito")
        else: print("la nota no se pudo borrar")
