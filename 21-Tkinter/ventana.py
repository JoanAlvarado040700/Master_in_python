'''
tkinter
Es un modulo para crear interfaces graficas de usuario.

'''


from tkinter import *
import os.path

class program():
    def __init__(self):
        self.title = "master en python"
        self.icon = "/imagenes/hacker.ico"
        self.icon_alt = "21-Tkinter/imagenes/hacker.ico"
        self.size = "777x480"
        self.resizable = False

    def cargar(self):
        # Crear una ventana Raiz
        ventana = Tk()
        self.ventana =ventana


        #Comprovar si existe una ruta
        ruta_ico = os.path.abspath(self.icon)

        # Mostrar texto en la ventana 
        texto = Label(ventana, text=ruta_ico)
        texto.pack()

        if not os.path.isfile(ruta_ico):
            ruta_ico = os.path.abspath(self.icon_alt)

        #titulo de la ventaba
        
        ventana.title(self.title)

        #Cambiar el tamaño de la ventana
        ventana.geometry(self.size)
        #icono de la ventana

        ventana.iconbitmap('21-Tkinter/imagenes/hacker.ico')


        #bloquear el tamañp de la ventana
        if self.resizable:
            ventana.resizable(0,1)
        else: ventana.resizable(0,0)

    def addtext(self):
            texto = Label(self.ventana, text="Hola desde un metodo")
            texto.pack()

    def mostrar(self):
            self.ventana.mainloop()

programa = program()


programa.cargar()
programa.addtext()
programa.mostrar()
