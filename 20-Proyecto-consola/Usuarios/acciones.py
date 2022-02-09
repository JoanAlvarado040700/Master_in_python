import Usuarios.users as modelo



class Acciones: 
    
    def registro(self):
        print("Ok!! vamos a registrarte en el sistema...")
        nombre = input("Introduce tu nombre:  ")
        apellido = input("Introduce tu apellido: ")
        email = input("Introduce tu correo electronico: ")
        password = input("Introduce tu contraseña: ")
        
        #Modelo
        
        usuario = modelo.User(nombre, apellido, email, password)
        registro = usuario.registro()

        if registro[0] >= 1:

            print(f"Perfecto {registro[1].nombre} te has registrado correctamente")

        else: print("Ups!! algo ha salido mal No se ha podido hacer el registro")

    
    def login(self):
        print("Perfecto !!!, vamos a verificar tus datos...")
        try:
            email = input("Introduce tu correo electronico: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.User('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]}, al sistema te has registrado el {login[5]}")

                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__) 
            print(f"Login incorrecto, vuelve a intentar")

    def proximasAcciones(self, usuario):
        print(""" 
            Acciones disponibles:
                1-> Crear notas
                2-> Mostrar notas
                3-> Eliminar notas
                4-> salir 
            
        """)
        
        accion = int(input("Que accion desea realizar? "))

        if accion == 1:
            print("vamos a crear")
            self.proximasAcciones(usuario) 


        elif accion == 2: 
            print("Mostrar notas ")
            self.proximasAcciones(usuario)

            
        elif accion == 3 : 
            print("Que nota desea eliminar?")
            self.proximasAcciones(usuario)


        elif accion == 4 : exit("Muchas gracias por usar nuestro sistema") 
        return None
