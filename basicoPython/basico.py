# Descripción: Ejemplo de tipos de datos en Python

cadena="Valor" #string
num=10 #int
num1=00.2 #float
num2=10+2j #complejo

print("Tipo: ",type(cadena))
print("Tipo: ",type(num))
print("Tipo: ",type(num1))
print("Tipo: ",type(num2))

# Descripción: Ejemplo de operaciones con tipos de datos en Python

num3=20
num4=10

suma=num3+num4 #suma
resta=num3-num4 #resta
multiplicacion=num3*num4 #multiplicación
division=num3/num4 #división
division_entera=num3//num4 #división entera
modulo=num3%num4 #módulo
potencia=num3**num4 #potencia

# Descripción: Operaciones binarias

# & and
# | or
# ^ exclusion
# ~ negacion
# << desplazamiento de bits izquierda
# >> desplazamiento de bits derecha

num5=10
print(num5 >> 1) # 1 indica el número de bits a desplazar
# En binario, 10 es 1010. Desplazar 1010 una posición a la derecha resulta en 0101, que es 5 en decimal.

print(num5 << 2) # 2 indica el número de bits a desplazar
# En binario, 10 es 1010. Desplazar 1010 dos posiciones a la izquierda resulta en 101000, que es 40 en decimal.

# Descripción: Cadena de texto
cadena1="Ejemplo de cadena de texto con comillas dobles"
cadena2='Ejemplo de cadena de texto con comillas simples'

print("Se pueden utilizar 'comillas' dentro de otra cadena de texto")
print("Concatenación "+"de"+" cadenas") #concatenación
print("Multiplicación "*2) #multiplicación de cadenas

# Descripción: Booleanos
print(True and False) #and
print(True or False) #or
print(not True) #negacion

# Descripción: Relacionales

# == igual
# != diferente
# > mayor que
# < menor que
# >= mayor o igual que
# <= menor o igual que
