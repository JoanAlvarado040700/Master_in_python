from tkinter import *
from PIL import Image, ImageTk #Se usa para importar imagenes a nuestra interface



ventana = Tk()
ventana.geometry("700x500")




texto = Label(ventana, text="Hola soy sebas !!") 

texto.config(
            fg = "white",
            bg= "#074855",
            padx= 300,
            pady = 5,
            font=("arial", 12),

)

texto.pack()


imagen = Image.open("./21-Tkinter/imagenes/laptop.png")
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack()


ventana.mainloop()





