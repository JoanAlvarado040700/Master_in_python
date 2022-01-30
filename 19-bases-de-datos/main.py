
import mysql.connector

#Conexion

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "master"
)


cursor = database.cursor(buffered=True)


#Crear tablas 

cursor.execute("""CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)

)
"""
)

#Insertar datos en una tabla 
'''

cursor.execute("INSERT INTO vehiculos VALUES(null,'opel','astra',1723.4 ) ")
database.commit()

'''

#Insertar de manera masiva 

'''

coches = [

    ("seat","ibiza",50000),
    ("Renault","Saxo",35000),
    ("mercedes","Clase C",24000)

]

cursor.executemany("INSERT INTO vehiculos VALUE(null,%s,%s,%s)", coches)
database.commit()
'''


cursor.execute("SELECT * FROM vehiculos ")

resul = cursor.fetchall()

for coche in resul:
    print(coche)


#Borrar datos 
#-----------------------------------------------------------
cursor.execute("DELETE FROM vehiculos WHERE precio> 45000")
database.commit()

print(cursor.rowcount, "Borrado !!")

#Actualizar datos

cursor.execute("UPDATE vehiculos SET modelo = 'Muy velozXD' WHERE modelo = 'Saxo' ")
database.commit()