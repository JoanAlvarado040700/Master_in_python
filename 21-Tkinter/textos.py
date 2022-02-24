from tkinter import *

ventana = Tk()
ventana.geometry("500x500")


def pruevas(nombre, apellido, pais):
    return f"hola {nombre} {apellido} veo que eres de {pais}"



texto = Label(ventana, text = pruevas("joan", "larios", "Nicaragua"))

texto.config(
            fg = "white",
            bg= "#074855",
            padx= 300,
            pady = 5,
            font=("arial", 12),

)


texto.pack(side=TOP, fill=Y, expand=YES)

ventana.mainloop()






