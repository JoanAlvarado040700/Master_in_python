from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Datos")

cab = Frame(ventana, width=200, height=50)

cab.config(
    bg="#074855",
    bd=2,
    relief=SOLID )

cab.pack(anchor=N,fill=X,expand=YES)
cab.pack_propagate(False)


encabezado = Label(cab,text= "Formularios con Tkinter")

encabezado.config(
            fg="black", # Color de las letras
            bg="darkgray", # color de fondo
            font =("Open sans",15), # Tipado de letras
            bd=2, relief=SOLID
)

encabezado.pack(anchor=CENTER)

#------------------------------------------------

cab = Frame(ventana, width=200, height=250)

cab.config(
    bg="#074855",
    bd=2,
    relief=SOLID )

cab.pack(side="top",anchor=W,fill=X,expand=YES)
cab.pack_propagate(False)

# ----------- Ingreso de datos 
texto= Label(cab,text="Ingresa un texto:")

texto.pack(side="top", anchor=CENTER)


def getDato():
    result.set(dato.get())
    if len(result.get()) < 1:
        resultado = Label(cab, text="No ha ingresado nada")
        resultado.pack()




dato = StringVar()
result = StringVar()

Label(cab, text= "Ingresa un texto...")
Entry(cab, textvariable= dato).pack(side="top", anchor=CENTER)

# -----------------------Salida de datos 

Button(cab, text= "Mostrar resultado", command=getDato).pack(side="top", anchor=CENTER)


cab = Frame(ventana, width=200, height=250)

cab.config(
    bg="#074855",
    bd=2,
    relief=SOLID )

cab.pack(side="top",anchor=W,fill=X,expand=YES)
cab.pack_propagate(False)


# ----------- resultados 
texto=Label(cab, text="Datos recogido:")
texto.config(
        bg="#074855",
        font=("bold",12),
        fg="black",
        pady=2
        )
texto.pack(anchor=CENTER,fill=X,expand=YES, side="top")
resultado = Label(cab,textvariable=result)

resultado.config(
            bg="#074855",
            fg ="white",
            font=("Consola",10)

)
resultado.pack(anchor=CENTER)




ventana.mainloop()