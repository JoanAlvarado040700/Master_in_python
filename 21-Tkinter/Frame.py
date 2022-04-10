from tkinter import *

ventana = Tk()


ventana.title("Marcos | curso de python")
ventana.geometry("700x500")


marco_padre = Frame(ventana, width=200, height=200)

marco_padre.config(
    bg="#074855"
  )

marco_padre.pack(side=BOTTOM,fill=X,expand=YES)



marco = Frame(marco_padre, width=200, height=200)

marco.config(
    bg="pink"
    )

marco.place(x = 100, y = 0)

marco = Frame(marco_padre, width=200, height=200)

marco.config(
    bg="green" )

marco.pack(side="right",anchor=SE)



marco_padre = Frame(ventana, width=200, height=200)

marco_padre.config(
    bg="#074855",
    bd=2,
    relief=SOLID )

marco_padre.pack(side=TOP,fill=X,expand=YES)
marco_padre.pack_propagate(False)

texto = Label(marco_padre, text="Curso de python")
texto.config(
    bg =  "#074855",
    padx= 300,
    pady = 5,
    font=("arial", 12),
)
texto.pack(side="left", expand=YES, fill=X)
ventana.mainloop()