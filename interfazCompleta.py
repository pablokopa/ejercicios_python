import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QGridLayout, QPushButton, QWidget, QHBoxLayout, QLabel

class interfazCompleta(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Interfaz Completa")
        self.setFixedSize(800, 800)

        cajaVertical = QVBoxLayout()  # Layout principal

# Creación de los botones superiores
        cajaHorizontal1 = QHBoxLayout()
        cajaVertical.addLayout(cajaHorizontal1)

        botonDataVault = QPushButton("Data Vault")
        botonSettings = QPushButton("Settings")
        botonHelp = QPushButton("Help")
        botonClose = QPushButton("Close")

        botonDataVault.setFixedHeight(130)
        botonSettings.setFixedHeight(130)
        botonHelp.setFixedHeight(130)
        botonClose.setFixedHeight(130)

        cajaHorizontal1.addWidget(botonDataVault)
        cajaHorizontal1.addWidget(botonSettings)
        cajaHorizontal1.addWidget(botonHelp)
        cajaHorizontal1.addWidget(botonClose)

# Creación del texto
        cajaHorizontal2 = QHBoxLayout()
        cajaVertical.addLayout(cajaHorizontal2)

        textoSpartan = QLabel("SPARTAN PASSWORD PROTECTOR")
        textoSpartan.setStyleSheet("font-weight: bold; font-size: 24px;")
        cajaHorizontal2.addWidget(textoSpartan)
        cajaHorizontal2.setAlignment(textoSpartan, Qt.AlignmentFlag.AlignCenter)

        contenedor = QWidget()  # Crear un widget contenedor
        contenedor.setLayout(cajaVertical)  # Establecer el layout vertical en el contenedor
        self.setCentralWidget(contenedor)  # Establecer el contenedor como el widget central de la ventana
        self.show()  # Mostrar la ventana

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)  # Crear la aplicación
    ventana = interfazCompleta()  # Crear la ventana principal
    aplicacion.exec()  # Ejecutar el bucle de eventos de la aplicación