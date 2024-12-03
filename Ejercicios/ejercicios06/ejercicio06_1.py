cadena = "Esto es una cadena"

def dousprimeiros ():
    print("- Dos primeros caracteres: " + cadena[:2])

def treultimos ():
    print("- Tres ultimos caracteres: " + cadena[-3:])

def cadadouscaracteres():
    print("- Cada dos caracteres: " + cadena[::2])

def inversa():
    print("- Cadena inversa: " + cadena[::-1])

def cadenaeinversa():
    print("- Cadena inversa y normal: " + cadena[::-1] + cadena)

dousprimeiros()
treultimos()
cadadouscaracteres()
inversa()
cadenaeinversa()