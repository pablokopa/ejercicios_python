cadena = "Cadena de texto 0123456789"
caracter = ","
cadena2  = "2552552550"
caracter2 = "."

def addcarcater ():
    print("- Añadir un carácter: " + caracter.join(cadena))

def reemplazar():
    print("- Reeplazar espacios por /: " + cadena.replace(" ", "/"))

def reeplazartodo():
    print("- Reemplazar todas las letras a por x: " + cadena.translate(str.maketrans("0123456789", "X" * 10)))

def insertcada3car():
    print("- Insertar un punto cada 3 caracteres: " + caracter2.join(cadena2[i:i+3] for i in range(0, len(cadena2), 3)))

addcarcater()
reemplazar()
reeplazartodo()
insertcada3car()