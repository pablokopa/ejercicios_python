import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel, QPushButton, QLineEdit
from _CaixaCor import CaixaColor


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        pallete = self.palette()
        pallete.setColor(QPalette.ColorRole.Window, QColor("lightpink"))
        self.setPalette(pallete)
        self.setWindowTitle("Ejercicio Libre")
        self.setMinimumSize(250, 250)

        layout = QGridLayout()

        # Crear y añadir textos
        textoNome = QLabel("Nome:")
        textoApelidos = QLabel("Apelidos:")
        textoDNI = QLabel("DNI:")
        textoEdade = QLabel("Edade:")

        layout.addWidget(textoNome, 0, 0, 1, 1)
        layout.addWidget(textoApelidos, 1, 0, 1, 1)
        layout.addWidget(textoDNI, 2, 0, 1, 1)
        layout.addWidget(textoEdade, 3, 0, 1, 1)


        # Crear y añadir TextLabels
        nomeInput = QLineEdit()
        apelidoInput = QLineEdit()
        dniInput = QLineEdit()
        edadInput = QLineEdit()

        layout.addWidget(nomeInput, 0, 1, 1, 1)
        layout.addWidget(apelidoInput, 1, 1, 1, 1)
        layout.addWidget(dniInput, 2, 1, 1, 1)
        layout.addWidget(edadInput, 3, 1, 1, 1)

        # Crear y añadir el botón al layout
        botonEditar = QPushButton("Editar")
        botonAceptar = QPushButton("Aceptar")
        botonCancelar = QPushButton("Cancelar")

        layout.addWidget(botonEditar, 4, 0, 1, 2)
        layout.addWidget(botonAceptar, 5, 0, 1, 2)
        layout.addWidget(botonCancelar, 6, 0, 1, 2)

        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    app.exec()