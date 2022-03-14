from tkinter import *


ventana = Tk()
ventana.geometry("600x600")


mi_menu = Menu(ventana)

ventana.config(menu = mi_menu)


archivo = Menu(mi_menu, tearoff=0)

archivo.add_command(label = "Nuevo archivo")
archivo.add_command(label = "Nueva ventana ")
archivo.add_separator()

archivo.add_command(label = "abrir archivo")
archivo.add_command(label = "abrir carpeta")
archivo.add_separator()
archivo.add_command(label = "Salir", command = quit)

mi_menu.add_cascade(label = "Archivo", menu = archivo)

mi_menu.add_command(label = "EDITAR")
mi_menu.add_command(label = "seleccionar")



ventana.mainloop()