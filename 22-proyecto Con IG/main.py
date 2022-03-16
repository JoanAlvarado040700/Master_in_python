from tkinter import *

'''

Crear un programa que tenga:
-ventana, listo
-tamaño fijo, listo
-no redimencionable, listo
-Un menu (Inicio, añadir, info, Salir)
-Diferentes pantallas
-Formulario de añadir productos
- Guardar datos temporalmente
-Mostrar datos listados 
opcion salir 
'''

# Ventana 
ventana = Tk()
ventana.geometry("700x500")
ventana.title("Proyecto master en python")
ventana.resizable(0,0)
#----------------------------------------------------

# ----------- MENU SUPERIOR ------------------------

menu = Menu(ventana)
menu.add_command(label = "inicio")
menu.add_command(label = "añadir")
menu.add_command(label = "informacion")
menu.add_command(label = "salir", command =ventana.quit)

ventana.config(menu = menu)




ventana.mainloop()