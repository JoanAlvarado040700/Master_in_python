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

