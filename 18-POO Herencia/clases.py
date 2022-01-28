#herrencia, es la posibilidad de compartir metodos y atributos 
# entre clases y que diferentes clases hereden de otras

from mailbox import NoSuchMailboxError


class persona:
    '''
    nombre
    apellido 
    altura 
    edad
    
    '''
    def getNombre(self):
        return self.nombre
    def getApellidos(self):
        return self.apellidos
    def getAltura(self):
        return self.altura
    def getEdad(self):
        return self.edad
    
    def setNombre(self, nombre):
        self.nombre = nombre
    def setApellidos(self,apellidos):
        self.apellidos = apellidos
    def setAltura(self,altura):
        self.altura = altura
    def setEdad(self,edad):
        self.edad = edad
    def hablar(self):
        return "Estoy hablando..."
    def dormir(self):
        return "Estoy dormido..."

class informatico(persona):
    '''
    lenguajes
    experiencia 

    '''

    def __init__(self) :
        self.lenguajes = "htlm, css, javaScrip, php"
        self.experiencia = 5
    
    def getlenguajes(self):
        return self.lenguajes

    def aprender(self,lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return "Estoy programando"
    def repararPC(self):
        return "He reparado tu pc"
    