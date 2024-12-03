# Lista de números
l = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generador de comprensión que calcula el cuadrado de cada número en la lista
x = (n**2 for n in l)

# Imprime el objeto generador
print(x)

# Itera sobre el generador e imprime cada valor generado (cuadrado de cada número)
for n in x:
    print(n)

# Definición de una función generadora que toma una lista como argumento
def mi_generador(l):
    # Itera sobre la lista y produce el cuadrado de cada número
    for n in l:
        yield n**2
# 'yield' es una palabra clave en Python utilizada para crear una función generadora.
# Cuando una función contiene la palabra clave yield, devuelve un objeto generador en lugar de un solo valor.

# Itera sobre el generador creado por la función mi_generador e imprime cada valor generado
for n in mi_generador(l):
    print("Mi generador dice " + str(n))



lista = list()
for elemento in x:
    lista.append(elemento)

tupla = tuple (mi_generador(l))
print(lista)
print(tupla)
