# EJERCICIOS DEL 1.1 AL 1.4

def nom_cadrados():
    print("Calcularanse potencia de dous números")
    n1 = input("Ingrese un número enteiro: ")
    n2 = input("Ingrese otro número enteiro: ")

    for x in range(int(n1), int(n2)):
        print("El cadrado de", x, "es:", x*x)

    print("\nEl valor final de x es: ", x)
    print("= Ejecución terminada =")

#nom_cadrados()

# EJERCICIO 1.5

def nombreYnumeros (nombre, num1, num2):
    print("Hola", nombre)
    print("El producto de", num1, "y", num2, "es igual a:", num1*num2)

#nombreYnumeros("Pablo", 5, 6)

# EJERCICIO 1.6

def perimetroRectangulo (base, altura):
    print("\nEl perímetro del rectángulo es:", 2*base + 2*altura)
    print("El área del rectángulo es:", base*altura)

def perimetroAreaCirculo(radio):
    print("\nEl perímetro del círculo es:", 2*3.1416*radio)
    print("El área del círculo es:", 3.1416*(radio*radio))

def volumenEsfera(radio):
    print("El volumen de una esfera es: ", 4/3*3.1416*(radio*radio*radio))

def areaRectangulo(ejeX1, ejeX2, ejeY1, ejeY2):
    print("El área del rectángulo según sus ejes es: ", (ejeX2-ejeX1)*(ejeY2-ejeY1))

def hipotenusaTrianguloRectangulo(cateto1, cateto2):
    print("La hipotenusa de un triángulo rectángulo es: ", ((cateto1*cateto1) + (cateto2*cateto2))**0.5)

# EJERCICIO 1.8

def factorial(n):
    fact = int(input("Ingrese un número entero: "))

    for i in range (1, n+1):
        fact = fact * i
    print("El factorial de", n, "es:", fact)

factorial(1)