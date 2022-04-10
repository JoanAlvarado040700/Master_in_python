from tkinter import *

'''

Crear un programa que tenga:
-ventana,-------- > listo
-tamaño fijo, -------- >listo
-no redimencionable,-------- > listo
-Un menu (Inicio, añadir, info, Salir), -------- > listo
-Diferentes pantallas,listo 
-Formulario de añadir productos, -------- > listo
- Guardar datos temporalmente
-Mostrar datos listados 
opcion salir, listo 
'''

# Ventana 
ventana = Tk()
ventana.geometry("350x450")
ventana.title("Proyecto master en python")
ventana.resizable(0,0)





#----------------------------------------------------


# Pantallas 

def home():
    
    home_label.config(
        fg= "white",
        bg= "black",
        font = ("Consola",30),
        padx = 120, pady = 20
    )


    home_label.place(x = 10, y = 10)  
    product_box.config(bg = "lightBlue1")
    product_box.place(x = 0, y = 0)

    for product in products:
        if len(product) == 3:
            product.append("Añadido!")
            Label(product_box, text= product[0]).place(x = 50, y = 120)
            Label(product_box, text= product[1]).place(x = 50, y = 150)
            Label(product_box, text= product[2]).place(x = 50, y = 170)
            Label(product_box, text="-------------------------").place(x = 10, y = 190)



    add_label.place_forget()
    info_label.place_forget()

    marco.place_forget()

    #--------------------------------------------------------------

def add():
    # Encabezando

    add_label.config(
        fg= "white",
        bg= "black",
        font = ("Consola",30),
        padx = 25, pady = 20
    )

    add_description_entry.config(
        width= 20, height= 5,
        font = ("Consola",15),
        padx = 10, pady = 18
    )

    
    #Formularios 
    marco.config(bg = "light blue")

    marco.place(x = 0, y = 0)

    add_name_label.place(x = 10, y = 100)
    add_name_entry.place(x = 100, y = 100)

    add_price_label.place(x = 10, y = 120)
    add_price_entry.place(x = 100, y = 120)

    add_description_label.place(x = 10, y = 150)
    add_description_entry.place(x = 100, y = 150)

    #--------------------------------------------------------------
    add_label.place(x = 10, y = 0)
    home_label.place_forget()
    info_label.place_forget()
    product_box.place_forget()
    # ----------------------------------------------------------------

    boton.place(x = 290, y = 310 )
def info():
    
    info_label.place(x = 10, y = 10)

    home_label.place_forget()
    add_label.place_forget()
    marco.place_forget()
    product_box.place_forget()

def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0","end-1c")

    ])
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)
    print(products)
    home()
#---------------------********             Variables         *******************************
products = []
name_data = StringVar()
price_data = StringVar()




#---------------------***************************************


# Definir campos de pantallas (INICIO)
product_box = Frame(ventana, width=350, height= 450)
home_label = Label(ventana, text = "Inicio")





#Definir campor de pantalla (ADD)

marco = Frame(ventana, width = 350, height = 450)
add_label = Label(marco, text = "Añadir producto")

# Campos de formularios 


add_name_label = Label(marco, text = "Nombre: ")
add_name_entry = Entry(marco,textvariable = name_data )
# ------------------------------
add_price_label = Label(marco, text = "Precio")
add_price_entry = Entry(marco,textvariable = price_data )

add_description_label = Label(marco, text = "Descripcion")
add_description_entry = Text(marco)

boton = Button(marco, text = "Guardar", command = add_product)




#Definir campo de pantalla  (INFO)
info_label = Label(ventana, text = "Creado por J. Sebastian 2022")





#Cargar pantalla de Inicio

home()

# ----------- MENU SUPERIOR ------------------------

menu = Menu(ventana)
menu.add_command(label = "inicio", command = home)
menu.add_command(label = "añadir", command = add)
menu.add_command(label = "informacion", command = info)
menu.add_command(label = "salir", command =ventana.quit)

ventana.config(menu = menu)








ventana.mainloop()