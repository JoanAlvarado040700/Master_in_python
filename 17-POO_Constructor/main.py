from personas import Person

persona = Person("Joan",1.57,"Verder")

def mostrarDatos(obj):
    n = 0
    for datos in obj:
        
        if n == 0: print(f"Nombre: {datos} ")
        if n == 1: print(f"color de ojos: {datos} ")
        if n == 2: print(f"Altura: {datos} " )
        n += 1



print("Objeto 1: ")

mostrarDatos(persona.getpresentar())

print("Objeto 2: ")

personas2 = Person("Sebas",1.57,"Negros")
mostrarDatos(personas2.getpresentar())

print(persona.getNumero(),"<-- Este es un atributo privado")

