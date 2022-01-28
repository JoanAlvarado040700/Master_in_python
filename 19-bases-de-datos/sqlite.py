# importar el modulo de sqlite3

import sqlite3
from tkinter import INSERT

#Conexion...
conexion = sqlite3.connect('pruevas.db')
#Crear cursor
cursor = conexion.cursor()

#Crear tabla: 

cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre varchar(255),
    descripcion text,
    precio int (255)
);
""")


#Guardar cambios
conexion.commit()
# -------------------------------------------------------

# Insertar datos..
'''
cursor.execute("INSERT INTO productos VALUES (null,'Primer producto','Descripcion de producto',150) ")
conexion.commit()

'''
#Insertar varios registros de golpe: 
productos = [
    ("portatil","en excelentes condiones",700),
    ("Celular inteligente","Perfecto para jugar ",400),
    ("Memoria RAM 8GB ","DDR3 con 3.600MH",45),
    ("Mause gamer","6 botones y es inalambrico",200)
]

cursor.executemany("INSERT INTO productos VALUES(null,?,?,?)",productos)
conexion.commit()
#Borrar registros

#cursor.execute("DELETE FROM productos")
#conexion.commit()
# -------------------------------------------------------

#Actualizar datos

cursor.execute("UPDATE productos  SET precio = 60 WHERE precio = 45  ")

#Listar datos: 
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

for producto in productos:
    print(producto)
'''
cursor.execute("SELECT precio FROM productos")
productos = cursor.fetchall()
for producto in productos:
    print(producto)

'''


# -------------------------------------------------------


# Cerrar la conexion
conexion.close()
