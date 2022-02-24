from tkinter import *

ventana = Tk()

ventana.geometry("700x500")

ventana.title("Formularios")

# texto de encabezado ventaba

encabezado = Label(ventana,text= "Formularios con Tkinter")

encabezado.config(
            fg="black", # Color de las letras
            bg="darkgray", # color de fondo
            font =("Open sans",15), # Tipado de letras
            pady = 10 # padding al eje y tambien se puede usar el padx
)

encabezado.grid(row=0, column=0, columnspan=10, padx=5,pady=5,sticky=NW)


# ----------- Nombres
texto= Label(ventana,text="Nombre:")
texto.grid(row=1, column=0, padx=5,pady=5, sticky=W)


campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, padx=5,pady=5)

#------------ Apellidos

texto= Label(ventana,text="Apellidos:")
texto.grid(row=2, column=0, padx=5,pady=5, sticky=W)


campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, padx=5,pady=5)

#---------- Descripcion:

texto= Label(ventana,text="Descripcion:")
texto.grid(row=3, column=0, padx=5,pady=5, sticky=N)


campo_texto_grande = Text(ventana)
campo_texto_grande.config(
            width=40,
            height=10, 
            font =("Consola", 12)
)
campo_texto_grande.grid(row=3, column=1, padx=5,pady=5, sticky=W)

botones = Button(ventana, text="Enviar")
botones.grid(row=4, column=1,sticky=W)
botones.config(
            fg = "white",
            bg = "#060447557",
            padx = 12,
            pady = 7,
)



 
ventana.mainloop()


