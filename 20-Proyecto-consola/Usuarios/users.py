
import datetime
import hashlib
import Usuarios.conexion as conexion


connect = conexion.conectar()
database = connect[0]
cursor = connect[1]
#print(database)

class User:

    def __init__(self,nombre,apellido,email,password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password

    def registro(self):
        fecha = datetime.datetime.now()

        #Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))


        sql = "INSERT INTO usuario VALUES (null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha)
        try:
            cursor.execute(sql, usuario)
            database.commit()  
            result = [cursor.rowcount,self ]   
        except:
            result = [0,self]
        return result    

    def identificar(self):
        #Consulta para comprovar que exista el usuario
        sql = "SELECT * FROM usuario WHERE email = %s AND password = %s"

        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))


        usuario = (self.email, cifrado.hexdigest())
        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result
    




        







