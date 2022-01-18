'''
Crear una lista con el contenido de esta tabla: 
Videojuegos: 

Accion  aventura deportes
GTA     ASSins      Fifa
COD     Crash       pes

Mostrar informacion ordenada

'''
juegos = [

    {
        "categoria": "accion",
        "nombre": ["GTA","COD"]
    },
    {
        "categoria": "aventura",
        "nombre": ["assins","crash"]
    },
    {
        "categoria": "deporte",
        "nombre": ["fifa","pes"]
    }

]


for n in range(0,3):
    print(f"Categoria:  {juegos[n]['categoria']} ") 
    print(f"Juego:  {juegos[n]['nombre']} ")



