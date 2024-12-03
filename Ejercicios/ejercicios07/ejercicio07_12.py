# APARTADO 1
def map(funcion, lista):
    return [funcion(x) for x in lista]

def cuadrado(x):
    return x * x

numeros = [1, 2, 3, 4, 5]
print(" Apartado 1:",map(cuadrado, numeros))

# APARTADO 2
def filter(funcion, lista):
    return [x for x in lista if funcion(x)]

def es_par(x):
    return x % 2 == 0

numeros = [1, 2, 3, 4, 5, 6]
print(" Apartado 2:",filter(es_par, numeros))