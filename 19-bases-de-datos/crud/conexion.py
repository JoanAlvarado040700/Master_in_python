import mysql.connector
from mysql.connector import Error

class DAD():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = '33060',
                user = 'root',
                password = '',
                db = 'cursos'
                
            )
        except Error as ex:
            print("Error al intentar la conexion: {0} ".format(ex))

    def listarCursos(self):
        if self.conexion.is_connected():
            try: 
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM curso ORDER BY nombre ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexion: {0} ".format(ex))
            




