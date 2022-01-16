#Acceder a indices:
peliculas = list(("batmas","Spiderman","Superman"))

print(peliculas[2])

#Modificar indice:

peliculas[1] = "Fanatico del tiempo"
print(peliculas)

#añadir elemento nuevo a la lista

peliculas.append("No manches frida") # append es para añadir elementos 
print(peliculas)

#Recorrer listas

print("-----------------LISTADO DE PELICULAS-------------")
nueva = ""
while nueva != "parar":
    nueva = input("Introduce la nueva pelicula: ")
    if nueva != "parar":
        peliculas.append(nueva)



for pelicula in peliculas:
    print(f" {peliculas.index(pelicula)}. {pelicula}  ")
    print("----------------")
