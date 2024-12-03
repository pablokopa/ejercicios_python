# Métodos listas
from avanzado import diccionario

lista = [1, 2, 3, ["Uno", "Dos", "Tres"]]

lista[2] = "Texto" # Cambia el valor de la posición 2
lista[3][1] = "Tres"
lista[1:3] = ["Uno", "Dos"] # Cambia los valores de las posiciones 1 y 2

lista.insert(2, "Nuevo") # Inserta un nuevo valor en la posición 2
lista.append("Último") # Añade un nuevo valor al final de la lista
lista.extend(["Otro", "Más"]) # Añade varios valores al final de la lista

lista.index("Texto") # Devuelve la posición del valor indicado
lista.index("Secuencia", 0, -1) # Devuelve la posición del valor indicado en el rango indicado

lista.remove("Texto") # Elimina el valor indicado
lista.pop(2) # Elimina el valor de la posición indicada

lista.reverse() # Da la vuelta a la lista

# Métodos diccionarios
diccionario["V"] = "Cinco" # Añade un nuevo valor al diccionario

diccionario.items() # Devuelve una lista de tuplas con clave y valor
diccionario.keys() # Devuelve una lista con las claves del diccionario
diccionario.values() # Devuelve una lista con los valores del diccionario
diccionario.get("V") # Devuelve el valor de la clave indicada
diccionario.pop("V") # Elimina la clave y el valor indicados
diccionario.items()

# Métodos cadenas
cadena = "El patio del colegio está cerrado"
caracter = ","

cadena.count('io', 8) # Cuenta el número de veces que aparece la secuencia 'io' a partir de la posición 8
cadena.find('io') # Devuelve la posición de la secuencia 'io'
cadena.partition('del') # Devuelve una tupla con la cadena dividida
cadena.replace('patio', 'jardín') # Reemplaza la secuencia 'patio' por 'jardín'
cadena.split(" ") # Divide la cadena en una lista de palabras
caracter.join(cadena) # Añade las palabras de la lista con el caracter indicado
