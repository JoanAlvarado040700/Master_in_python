from tkinter import *
from tkinter import messagebox as ms
ventana = Tk()
ventana.geometry("700x200")
ventana.resizable(False,False)
ventana.config(
        relief= "groove",
        bd = 3
)
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




def sumar():
        resultado.set(float(numero1.get()) + float(numero2.get()))
def resta():
        resultado.set(float(numero1.get()) - float(numero2.get()))
def multiplicar():
        resultado.set(float(numero1.get()) * float(numero2.get()))
def dividir():
        resultado.set(float(numero1.get()) / float(numero2.get()))
def mostrar():
        ms.showinfo("Resultados","El resultado de la operacion es: {resultado.get()} ")


numero1 = StringVar()
numero2 = StringVar()

resultado = StringVar()


#-------------------------------------------


num = Entry(cuadro,bd= 2, textvariable = numero1 ) # --------- > Dato 1

num.place(x = 150, y= 10) # Entrada de texto

texto = Label(cuadro, text= "Ingrese un valor !")
texto.config(
        fg = "black",
        bg = "#007450",
        font = ("bold",12)

)
texto.place(x=10, y= 55)

num2 = Entry(cuadro,bd= 2, textvariable = numero2)

num2.place(x = 150, y= 57) 




# ---------------- Botones especiales



boton = Button(cuadro, bd=5, text= "Suma ", width=8, height=2, activebackground="sky blue", command= sumar)
boton.place(x= 20, y=90)

boton = Button(cuadro, bd=5, text= "Resta",width=8, height=2,activebackground="sky blue", command= resta)
boton.place(x= 95, y=90)

boton = Button(cuadro, bd=5, text= "Multiplicar",width=8, height=2,activebackground="sky blue", command = multiplicar)
boton.place(x= 170, y=90)

boton = Button(cuadro, bd=5, text= "Dividir",width=8, height=2,activebackground="sky blue", command = dividir)
boton.place(x= 245, y=90)

#  *****************************************************************************


cuadro = Frame(contenido, width=350, height=450)
cuadro.config(
        bg = "#084256645"
)
cuadro.pack(side = "left",anchor=NE)
cuadro.pack_propagate(False)



#-----------  salida de resultados ---------------------

texto = Label(cuadro, textvariable = resultado)
texto.config(
        fg = "white",
        bg = "#084256645",
        font = ("bold",12)

)
texto.pack(side = "left",anchor = CENTER)




#******************************************************************************





ventana.mainloop()