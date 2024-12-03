# Declaración de función con dos parámetros
print("\n====Función de prueba====")

def nombreFuncion (parametro1, parametro2):
    print(parametro1)
    print(parametro2)

# Llamada a la función
nombreFuncion("Hola", "Mundo")

# Función suma con un parámetro con valor por defecto (operador2 = 4)
print("\n====Función suma====")

def suma (operador1, operador2: int = 4):
    print("La suma es: ", operador1+operador2)

suma(3,4) # Se toman los valores de los dos parámetros indicados
suma(8) # Se toma el valor por defecto de operador2

# Función imprimir con dos parámetros con valor por defecto
print("\n====Función imprimir====")
def imprimir (texto="Hola", veces=3):
    print(veces*texto)

imprimir("Jamón", 2) # Imprime el texto seleccionado el número de veces indicado
imprimir(veces=5) # Imprime el texto el número de veces indicado


# ========== FUNCIONES DE ORDEN SUPERIOR ==========
# Funciones dentro de funciones

def saudar(lingua):
    # Definición de funciones para cada idioma
    def saudar_en():
        print("Hello")

    def saudar_es():
        print("Hola")

    def saudar_fr():
        print("Salut")

    def saudar_gl():
        print("Ola")

    # Diccionario que mapea el código del idioma a la función correspondiente
    lingua_func = {
        "es": saudar_es,
        "en": saudar_en,
        "fr": saudar_fr,
        "gl": saudar_gl
    }

    # Retorna la función correspondiente al idioma especificado
    return lingua_func[lingua]

# Llamada a la función saudar con el idioma "es" (español)
saudar("es")()

# Llamada a la función saudar con el idioma "fr" (frances)
saudar("fr")()