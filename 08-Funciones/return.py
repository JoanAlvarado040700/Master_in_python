# Ejemplo parametros opcionales y el return 

def calculadora(numero1,numero2,operacion = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    div = numero2 / numero1

    cadena = ""

    cadena += "Suma: " +str(suma)
    cadena +="\n"
    cadena += "resta: " + str(resta)
    cadena +="\n"
    cadena += "Multiplicacion: " +str(multi)
    cadena +="\n"
    cadena += "Divicion: " + str(div)
    cadena +="\n"

    return cadena

print(calculadora(6,7))