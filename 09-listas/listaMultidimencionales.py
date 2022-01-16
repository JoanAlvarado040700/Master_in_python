# Crear listas multidimencionales:

print("-----------Listas de contactos --------------")

contactos = [
    [
        "Juanito",
        "juanito@gmail"
    ],
    [
        "pedra",
        "pedra@gmail.com"
    ],
    [
        "Jonny tetz",
        "test@.Yahoo.com"
    ]


]

#print(contactos[2][1])

for contacto in contactos:
    print("------------------------------")
    print(f"Contacto numero:  {contactos.index(contacto)} ")
    for elementos in contacto:
        if contacto.index(elementos) == 0:
            print( f"Nombre: {elementos} ")
        else:
            print(f"EMail: {elementos} ")