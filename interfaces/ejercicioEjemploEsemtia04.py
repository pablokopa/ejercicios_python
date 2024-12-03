import sys
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout

class CaixaColor(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(self.backgroundRole(), color)
        self.setPalette(paleta)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout Colores")
        self.setMinimumSize(800, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)

        # Crear layout vertical 1
        cajaVertical1 = QVBoxLayout()
        cajaVertical1.addWidget(CaixaColor(QColor("red")))
        cajaVertical1.addWidget(CaixaColor(QColor("yellow")))
        cajaVertical1.addWidget(CaixaColor(QColor("purple")))
        main_layout.addLayout(cajaVertical1)

        # Crear layout horizontal
        main_layout.addWidget(CaixaColor(QColor("green")))

        # Crear layout vertical 2
        cajaVertical2 = QVBoxLayout()
        cajaVertical2.addWidget(CaixaColor(QColor("red")))
        cajaVertical2.addWidget(CaixaColor(QColor("purple")))
        main_layout.addLayout(cajaVertical2)

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Creamos la aplicación
    window = MainWindow()  # Creamos la ventana principal
    window.show()  # Mostramos la ventana principal
    sys.exit(app.exec())  # Ejecutamos el bucle de eventos de la aplicación