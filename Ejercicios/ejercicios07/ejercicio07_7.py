class ErroDNI(Exception):
    def __init__(self, dni):
        if len(dni)!=9:
            self.mensaxeErro = "non ten 9 dixitos"
        elif not dni[0:-1].isdigit():
            self.mensaxeErro = "os 8 primeiros dixitos teñen que ser números"
        elif dni[-1].isalpha():
            self.mensaxeErro = "o último dixito ten que ser unha letra"
        else:
            print("Formato de DNI correcto")
    def __str__(self):
        return "O DNI ten un formato incorrecto, a razón é que " + self.mensaxeErro

def exercicio7(listaNomes):
    for persoa in listaNomes:
        if len(persoa[3])!=9:
            raise ErroDNI(persoa[3])
        elif not persoa[3][0:-1].isdigit():
            raise ErroDNI(persoa[3])
        elif persoa[3][-1].isalpha():
            raise ErroDNI(persoa[3])
        else:
            print("Formato de DNI correcto")

try:
    exercicio7([('Pablo', 'Iglesias', 'Leyenda', '12345678D'), ('Pepe', 'Perez', 'Hernandez', '36789123K')])
except ErroDNI as e:
    print("Parece que ocurre un erro: " + str(e))