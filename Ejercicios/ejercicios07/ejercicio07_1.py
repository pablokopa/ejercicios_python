tupla = (1, 2, 3, 4, 5)

def tuplaordenada():
    for i in range (1, len(tupla)):
        if tupla[i] < tupla[i-1]:
            return False
    return True

print(tuplaordenada())