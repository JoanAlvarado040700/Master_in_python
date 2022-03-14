from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.config(
        bg= "LightCyan2",
        bd = 5, 
        relief= "groove"
)

class partes:
    def cabecera():
                
        cab = Frame(ventana, width=200, height=50)
        cab.config(
                bg = "CadetBlue3"
        )

        cab.pack(anchor=N, fill = X,expand=YES)
        cab.pack_propagate(False)

        titulo = Label(cab, text="Formularios 2")
        titulo.config(
                fg = "#000000",
                bg = "CadetBlue3",
                font = ("Consola",20),
                pady = 7
        )

        titulo.pack(anchor=CENTER)

programa = partes()

partes.cabecera()
#--------------------------------------------------------------
#--------------- FUNCIONES 


def MostrarProfe():
        texto = ""
        if des.get() == False:
                if web.get():
                        texto += "Desarrollo web"
                if movil.get():
                        if web.get():
                                texto += " y Desarrollo movil"
                        else: texto += "Desarrollo Movil"
                if des.get():
                        texto += "Desempleado"
                        if web.get():
                                texto += ""
                        if movil.get(): texto += ""
                
        else: texto += "DESEMPLEADO"
        Mostrar.config(
                text = texto,
                font = ("Arial",14)

        )

# ------------------------------

def marcar():
        marcado.config(text = opc.get())

# ------------------------------

def seleccionar():
        eleccion.config(text = opcion.get())

# -------------------------------------------------
# Checkbutton

Label(ventana, text = " Oye a que te dedicas ?", font = ("Arial",14)).place(x=10, y=70)

web = IntVar()
movil = IntVar()
des = IntVar()

Checkbutton(
        ventana,
        text= "Desarrollador web",
        font = ("Arial",14),
        variable = web, onvalue=1, offvalue= 0, 
        command = MostrarProfe
        ).place(x=10, y= 100)

Checkbutton(
        ventana,
        text= "Desarrollador Movil",
        font = ("Arial",14),
        variable = movil, onvalue=1, offvalue= 0, command = MostrarProfe
        ).place(x=10, y= 135)

Checkbutton(ventana, text= "Desempleado",font = ("Arial",14), variable = des, onvalue=1, offvalue= 0, command = MostrarProfe).place(x=250, y= 100)


Mostrar = Label(ventana)
Mostrar.place(x = 10, y = 172 )

#------------------------------------------------------------------------------------

# ------------------------------- RADIO BUTTON --------------------------------

opc = StringVar()
opc.set(None)
Label(ventana, text = "Cual es tu genero? ",font = ("Arial",14)).place(x = 10, y= 220)

Radiobutton(ventana, 
        text = "Masculino",value = "Masculino",
        font = ("Arial",14), variable = opc,command = marcar
        ).place(x = 10, y= 257)
Radiobutton(ventana,
        text = "Femenino", value = "Femenino",
        font = ("Arial",14),variable = opc, command = marcar
        ).place(x = 10, y= 294)
marcado = Label(ventana)
marcado.place(x = 10, y = 330)


# ----------------------------------------------------------------
# -------------------------------- OPTION MENU --------------------------------


Label(ventana, text = "Selecciona una opcion ",font = ("Arial",14)).place(x = 250, y= 220)
opcion = StringVar()
opcion.set("Opcion 1")


select =  OptionMenu(ventana, opcion, "opcion 1", "opcion 2", "opcion 3", "opcion 4")
select.place(x = 250, y = 257)
Button(ventana, text = "ver", command = seleccionar).place(x = 430, y = 300)

eleccion = Label(ventana)
eleccion.place(x = 250, y = 300)


ventana.mainloop()