#Constructores: 


class Person:
    altura = 1.75
    color_ojos = "azules"
    nombre = "Juanito"
    peso = 65
    __numero = 86377856
    #Caracteristicas de una persona u objetos 
    #---------------------------------
    def __init__(self,nombre,altura,color_ojos):
        self.nombre = nombre
        self.altura = altura
        self.color_ojos = color_ojos
    

    #metodos:
    def getNumero(self):
        return self.__numero
    def setpresentar(self,nombre,color_ojos,altura):
        self.nombre = nombre
        self.color_ojos = color_ojos
        self.altura = altura
    def setbajarPeso(self,peso):
        print("Ejercitandose...")
        self.peso = peso
    def getpresentar(self):
        return self.nombre, self.color_ojos, self.altura
    def getbajarPeso(self):
        return self.peso

        

