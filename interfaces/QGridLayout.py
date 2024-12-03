import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel
from _CaixaCor import CaixaColor
from ejercicioEjemploEsemtia04 import MainWindow

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo Grid Layout")
        self.setMinimumSize(800, 400)

        maia = QGridLayout()
        maia.addWidget(CaixaColor("red"))
        maia.addWidget(CaixaColor("blue"), 0, 1, 1, 2)
        maia.addWidget(CaixaColor("green"), 1, 0, 2, 1)
        maia.addWidget(CaixaColor("pink"), 1, 1, 1, 2)
        maia.addWidget(CaixaColor("orange"), 2, 1, 1, 1)
        maia.addWidget(CaixaColor("yellow"), 2, 2, 1, 1)
        # Row: en la que se encuentra, column: en la que se encuentra, rowSpan: filas que ocupa, columnSpan: columnas que ocupa

        contenedor = QWidget()
        contenedor.setLayout(maia)
        self.setCentralWidget(contenedor)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    app.exec()


'''
class EjercicioEsemtia(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejercicio Esemtia")
        self.setMinimumSize(800, 400)

        maia = QGridLayout()
        maia.addWidget(CaixaColor("red"), 0, 0, 2, 1)
        maia.addWidget(CaixaColor("yellow"), 2, 0, 2, 1)
        maia.addWidget(CaixaColor("purple"), 4, 0, 2, 1)

        maia.addWidget(CaixaColor("darkgreen"), 0, 1, 6, 1)

        maia.addWidget(CaixaColor("red"), 0, 2, 3, 1)
        maia.addWidget(CaixaColor("purple"), 3, 2, 3, 1)

        # Row: en la que se encuentra, column: en la que se encuentra, rowSpan: filas que ocupa, columnSpan: columnas que ocupa

        contenedor = QWidget()
        contenedor.setLayout(maia)
        self.setCentralWidget(contenedor)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    app.exec()
'''