import sys
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class PrimeraVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Primera Ventana")
        self.setMinimumSize(200, 100)
        self.setMaximumSize(200, 100)

        # Establecer color de fondo rojo
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("orange"))
        self.setPalette(paleta)

        # Crear botón para abrir la segunda ventana
        self.boton = QPushButton("Abrir Segunda Ventana")
        self.boton.clicked.connect(self.abrir_segunda_ventana)

        # Crear layout y añadir el botón
        layout = QVBoxLayout()
        layout.addWidget(self.boton)

        # Crear contenedor y establecer el layout
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

    def abrir_segunda_ventana(self):
        # Crear instancia de la segunda ventana y mostrarla
        self.segunda_ventana = SegundaVentana(self)
        self.segunda_ventana.show()
        self.hide()  # Ocultar la primera ventana

class SegundaVentana(QMainWindow):
    def __init__(self, primera_ventana):
        super().__init__()

        self.primera_ventana = primera_ventana

        self.setWindowTitle("Segunda Ventana")
        self.setMinimumSize(200, 100)
        self.setMaximumSize(200, 100)

        # Establecer color de fondo amarillo
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("lightgreen"))
        self.setPalette(paleta)

        # Crear botón para regresar a la primera ventana
        self.boton = QPushButton("Regresar a la Primera Ventana")
        self.boton.clicked.connect(self.regresar_a_primera_ventana)

        # Crear layout y añadir el botón
        layout = QVBoxLayout()
        layout.addWidget(self.boton)

        # Crear contenedor y establecer el layout
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

    def regresar_a_primera_ventana(self):
        # Mostrar la primera ventana y cerrar la segunda
        self.primera_ventana.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    primera_ventana = PrimeraVentana()
    primera_ventana.show()
    sys.exit(app.exec())