def funcion_necesita_decorador():
    print("Decorame por favor!")

def mi_decorador(funcion_a_decorar):
    def funcion_envolvente():
        print("\nOperaciones antes de la funcion a decorar")
        funcion_a_decorar()
        print("Operacions posteriores a execución da función a decorar")
    return funcion_envolvente()

def mi_decorador2(funcion_a_decorar):
    def funcion_envolvente():
        print("\nOperaciones antes de la funcion a decorar")
        funcion_a_decorar()
        print("Operacions posteriores a execución da función a decorar")
    return funcion_envolvente()

mi_decorador(funcion_necesita_decorador)


@mi_decorador2
def funcion2_necesita_decorador():
    print("Eu tamén preciso que me decoren!")