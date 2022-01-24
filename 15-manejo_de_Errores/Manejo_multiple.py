#Manejo multiple de excepciones

try:
    num = int(input("Numero para elevar al cuadrado: "))

    print("El cuadrado es: "+ str(num**2))
except TypeError:
    print("Debes de convertir tus cadenas a enteros")
#except ValueError:
#   print("Introduce un numero correcto")
except Exception as e:
    print("ha ocurrido un error : ", type(e).__name__)

    
