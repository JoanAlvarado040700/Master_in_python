import clases

persona = clases.persona()

persona.setNombre("Joan")
persona.setApellidos("Larios")

print(f"Mi nombre es: {persona.getNombre()} {persona.getApellidos()}  ")
print(persona.hablar())

informatic = clases.informatico()

informatic.setNombre("Sebastian")
informatic.setApellidos("Alvarado")

print(f"El informatico es:  {informatic.getNombre()} {informatic.getApellidos()} ")
print(informatic.getlenguajes())