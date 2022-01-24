# Programacion orientada a objetos

# Definir  una clase: 

class Person:
    altura = 1.75
    color_ojos = "azules"
    nombre = "Juanito"
    peso = 65
    #Caracteristicas de una persona u objetos 
    #---------------------------------

    #metodos:
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


#Crear un objeto

persona = Person()

print("Peso actual: ", persona.getbajarPeso(), "Kg")
persona.setbajarPeso(60)
print("El peso actual: ", persona.getbajarPeso()) 


#Crear mas objetos 

#objeto 1: 

print("Objeto 1: ")
def mostrarDatos(obj):
    n = 0
    for datos in obj:
        
        if n == 0: print(f"Nombre: {datos} ")
        if n == 1: print(f"Color de ojos: {datos} ")
        if n == 2: print(f"Altura: {datos} " )
        n += 1

mostrarDatos(persona.getpresentar())
print("************************************************")
print("Objeto 2: ")
persona2 = Person()
persona2.setpresentar("Sebastian","Negros",157)
mostrarDatos(persona2.getpresentar())