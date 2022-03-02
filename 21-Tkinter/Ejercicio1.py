from tkinter import *

ventana = Tk()
ventana.geometry("700x155")

# -------------------  Cabecera ----------------
cab = Frame(ventana, width=200, height=50)
cab.config(
        bg = "#007450"
)

cab.pack(anchor=N, fill = X,expand=YES)
cab.pack_propagate(False)

titulo = Label(cab, text="Mini Calculadora")
titulo.config(
        fg = "#000000",
        bg = "#007450",
        font = ("Consola",20)
)
titulo.pack(anchor=CENTER)

#------------------ Contenido de la mini calculadora ---------------------------


contenido = Frame(ventana, width=200, height=450)
contenido.config(
        bg = "darkgray",
        relief =SOLID,
        bd=4

)

contenido.pack(anchor=N, fill = X,expand=YES)
contenido.pack_propagate(False)



# ------------------ Cuadros de contenido --------------------------------


#  *****************************************************************************

cuadro = Frame(contenido, width=350, height=450)
cuadro.config(
        bg = "#007450"
)
cuadro.pack(side= "left", anchor=NW)
cuadro.pack_propagate(False)



texto = Label(cuadro, text= "Ingrese un valor !")
texto.config(
        fg = "black",
        bg = "#007450",
        font = ("bold",12)

)
texto.place(x=10, y= 8)


#----------- Funciones ----------------------


#def getDatos():



#-------------------------------------------


num = Entry(cuadro,bd= 2 ) # --------- > Dato 1

num.place(x = 150, y= 10) # Entrada de texto

texto = Label(cuadro, text= "Ingrese un valor !")
texto.config(
        fg = "black",
        bg = "#007450",
        font = ("bold",12)

)
texto.place(x=10, y= 55)

num2 = Entry(cuadro,bd= 2)

num2.place(x = 150, y= 57) # Entrada de texto


#  *****************************************************************************


cuadro = Frame(contenido, width=350, height=450)
cuadro.config(
        bg = "#084256645"
)
cuadro.pack(side = "left",anchor=NE)
cuadro.pack_propagate(False)



#-----------  Boton y salida de resultados ---------------------

boton = Button(cuadro, bd=5, text= "Resultado")
boton.pack(side= "top", anchor=CENTER)

texto = Label(cuadro, text = "Resultado")
texto.config(
        fg = "white",
        bg = "#084256645",
        font = ("bold",12)

)
texto.place(x= 90, y= 50)




#******************************************************************************





ventana.mainloop()