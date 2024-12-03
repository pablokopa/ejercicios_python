ficha1 = (3,4)
ficha2 = (4,5)

cadenafichas = "3-1 2-5"

def encajatuplas():
    if ficha1[0]==ficha2[0] or ficha1[0]==ficha2[1] or ficha1[1]==ficha2[0] or ficha1[1]==ficha2[1]:
        print("\nLa ficha " + str(ficha1) + " y la ficha " + str(ficha2) + " encajan")
    else:
        print("\nLa ficha " + str(ficha1) + " y la ficha " + str(ficha2) + " no encajan")

def encajacadena():
    ficha3 = cadenafichas.split(" ")[0]
    ficha4 = cadenafichas.split(" ")[1]
    if ficha3[0] == ficha4[0] or ficha3[0] == ficha4[2] or ficha3[2] == ficha4[0] or ficha3[2] == ficha4[2]:
        print("La ficha " + str(ficha3) + " y la ficha " + str(ficha4) + " encajan")
    else:
        print("La ficha " + str(ficha3) + " y la ficha " + str(ficha4) + " no encajan")

encajatuplas()
encajacadena()