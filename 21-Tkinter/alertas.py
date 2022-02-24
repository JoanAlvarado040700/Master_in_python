from tkinter import *
from tkinter import messagebox as Messagebox

ventana = Tk()
ventana.geometry("700x500")

def alerta():
    Messagebox.showerror("Alerta","Hola este es el curso de python")
def salir():
    respuesta = Messagebox.askquestion("Salir", "Desea salir del programa? ")

    if respuesta != "no":
        ventana.destroy()
Button(ventana,text="Mostrar alerta", command=alerta).pack()


Button(ventana,text="Salir", command=salir).pack()





ventana.mainloop()

