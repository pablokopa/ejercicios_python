import math

# Clase Punto
class Punto:
    """Clase que define un punto bidimensional no primero cuadrante"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return ("A coodernada x é: " + str(self.x) + "\nA coordenada y é: " + str(self.y))

# Clase Circulo que hereda de Punto
class Circulo (Punto):
    def __init__(self, x=0, y=0, r=0):
        Punto.__init__(self,x,y)
        self.r = 0

    def perimetro(self):
        return 2* math.pi * self.r

    def area(self):
        return math.pi * math.pow(self.r,2)

    def __str__(self):
        return (Punto.__str__(self) + "\n\n======== RADIO Y PERIMETRO CIRCULO ========\nO radio de círculo é: " + str(self.r))

# Clase Punto2 que hereda de Punto
class Punto2 (Punto):
    def __init__(self, x=0, y=0):
        self.__x = self.setX(x)
        self.__y = self.setY(y)

    def getX (self):
        return self.__x

    def getY (self):
        return self.__y

    def setX (self, x):
        if x>=0:
            self.__x = x
        else:
            raise NonPrimeroCuadranteError

    def setY (self, y):
        if y>=0:
            self.__y = y
        else:
            raise NonPrimeroCuadranteError

    def __coordenadas (self):
        return ("As coordenadas son: (" + str(self.__x) + ", " + str(self.__y) + ")")

    def __str__(self):
        return ("\n======== COORDENADAS PUNTO 2 ========\nA coodernada x é: " + str(self.__x) + "\nA coordenada y é: " + str(self.__y))


# Excepción
class NonPrimeroCuadranteError(Exception):
    def __str__(self):
        return "Erro de coordenadas fora do 1º cuadrante"


# Creación de un objeto de la clase Punto
p1 = Punto()
p1.x = 5
p1.y = 10
print(p1)

# Creación de un objeto de la clase Circulo
c1= Circulo()
print(c1)
print("O perímetro do círculo é: " + str(c1.perimetro()))

# Creación de un objeto de la clase Punto2
p2 = Punto2(235,2) # Salta una excepcion si se pone un número negativo
print(p2)
print(p2._Punto2__coordenadas()) # Imprime las coordenadas del punto

# Creación de objeto con excepción
try:
    p2 = Punto2()
    p2.x = 4
    p2.y = -3
except NonPrimeroCuadranteError:
    print("Excepcion")