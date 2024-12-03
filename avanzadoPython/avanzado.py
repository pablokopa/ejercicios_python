# Descripción: Uso de listas en Python

print("====== Uso de listas en Python ======")
l = [1, 2, 3, 4, 5]
print(l[2]) # Impresión de un elemento de la lista

l2= [1, "Dous", 3.0, [4, 'Cinco'], 6, 7, 8]
print(l2[3][1]) # Impresión de un elemento de una lista dentro de otra lista
print(l2[1][2]) # Impresión de un caracter de un string dentro de una lista
print(l2[1:3]) # Impresión de varios elementos de la lista
print(l2[1:7:2]) # Impresión de varios elementos de la lista con un salto de 2

l2[5:7] = ['Siete', 'VIII'] # Modificación de un elemento de la lista
print(l2)
print(type(l), "\n")

# Descripción: Uso de tuplas en Python

print("====== Uso de tuplas en Python ======")
t=(1, 2.0, "Tres", [4, "Cadena"], 5) # Tupla
t2=(1,) # Tupla de un solo elemento
print(type(t), "\n")

# Descripción: Uso de diccionarios en Python

print("====== Uso de diccionarios en Python ======")
diccionario = {
    2.0 : 2,
    "Dous" : 2, # Clave y valor
    3.0 : 3,
    "Catro" : 4,
    5 : 5,
    "v" : 5
}

print (diccionario[2.0]) # Impresión de un valor del diccionario
print (diccionario["Catro"])
print(type(diccionario), "\n")

# Descripción: Uso de If-else en Python
print("====== Uso de If-else en Python ======")

variable = 3
if variable == 5:
    print("La variable es: " + str(variable))
    print("Dentro del if")
elif variable == 3:
    print("La variable es: " + str(variable))
    print("Dentro del elif")
else:
    print("La variable no es 5")

par = True if variable % 2 == 0 else False # Operador ternario

# Descripción: Uso de While en Python
print("\n====== Uso de While en Python ======")

variable2 = 5
while variable2 < 6:
    print("La variable es: " + str(variable2))
    variable2 = variable2 + 1 # Incremento de la variable (variable2 += 1)

i=0
while True:
    print("Instrucciones que se hacen al menos una vez, neste caso: " + str(i+1))
    i=i+1
    if i<5:
        continue
    else:
        break


# Descripción: Uso de For en Python
print("\n====== Uso de For en Python ======")

# Recorrido de una lista
print("Recorrido de una lista:")
lista = [1, 2, 3]
for i in lista:
    print(i)

longitudLista = len(lista) # Longitud de la lista

# Recorrido de un rango entre 0 y 5
print("\nRecorrido de un rango entre 0 y 5:")
for i in range(5):
    print(i)

# Recorrido de un rango entre 0 y 5
print("\nRecorrido de un rango entre 6 y 12 con un salto de 2:")
for i in range(6, 12, 2): # Rango entre 6 y 12 con un salto de 2
    print(i)

# Recorrido de una lista con índice
print("\nRecorrido de una lista con índice")
for indice, elemento in enumerate(lista):
    print("El índice es: " + str(indice))
    print("El elemento es: " + str(elemento))

# Crear lista con valores multiplicados (lista2) y valores filtrados (lista3)
lista1= [1, 2, 3, 4, 5]
lista2= [num*2 for num in lista1] # Multiplica los valores de lista1 por 2
lista3 = [n for n in lista1 if n>2] # Filtra elementos de lista1 (solo los elementos mayores que 3)
print(lista1)
print(lista2)
print(lista3)

# Funciones lambda
l = [0, 1, 2, 3]
m = ['a', 'b', 'c']
n = [r*s for s in l
         for r in m
            if s>0]
q= [ (lambda r, s : r*s) (r, s) for s in l
                                for r in m
                                if s>0]
