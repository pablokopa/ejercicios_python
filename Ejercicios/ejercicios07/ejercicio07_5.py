from math import factorial

listaNums = [-2, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ====== NÚMEROS PRIMOS ======
# Función que determina si un número es primo
def esPrimo(n):
    if n <= 1:
        return False
    # Verifica si el número es divisible por algún número desde 2 hasta la raíz cuadrada de n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Función que imprime los números primos de una lista
def numerosPrimos():
    for num in listaNums:
        if esPrimo(num):
            print(num, "es un número primo")

# ====== SUMATORIO Y PROMEDIO ======
def sumatorioymedia():
    suma = 0
    contador = 0
    for num in listaNums:
        if esPrimo(num):
            suma += num
            contador = contador + 1
    media = suma / contador
    print("\nLa suma total de todos los números primos es", suma)
    print("La media es de", media)

# ====== FACTORIAL ======
def factorialnums():
    factoriales = [factorial(num) for num in listaNums if esPrimo(num)]
    print("\nLista de factoriales de números primos:", factoriales)
    return factoriales

# ====== EXCEPCIONES ======
class NumeroNegativo (Exception):
    def __str__(self):
        return "Hay un número negativo"

numerosPrimos()
sumatorioymedia()
factorialnums()