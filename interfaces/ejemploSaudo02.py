import sys
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurar la ventana
        self.setWindowTitle("Saludo")  # Título de la ventana
        self.setMinimumSize(200, 100)  # Tamaño mínimo de la ventana
        self.setMaximumSize(200, 100)  # Tamaño máximo de la ventana

        # Cambiar el color de fondo
        pallete = self.palette()
        pallete.setColor(QPalette.ColorRole.Window, QColor("lightgrey"))  # Cambiar color de fondo
        self.setPalette(pallete)  # Aplicar paleta de colores

        # Creación de botones y cuadros de texto
        self.textoLabel = QLabel("Introduce tu nombre:")  # Crear label con el texto inicial
        self.nombreInput = QLineEdit()  # Crear campo de texto para la entrada del nombre
        self.botonSaludar = QPushButton("Saludar")  # Crear botón con el texto "Saludar"
        self.botonSaludar.clicked.connect(self.saludar)  # Conectar señal clicked del botón a saludar()
        self.nombreInput.returnPressed.connect(self.saludar)  # Para que funcione cuando se pulsa Enter

        # Creación de layout
        layout = QVBoxLayout()  # Crear layout vertical
        layout.addWidget(self.textoLabel)  # Añadir label al layout
        layout.addWidget(self.nombreInput)  # Añadir campo de texto al layout
        layout.addWidget(self.botonSaludar)  # Añadir botón al layout

        container = QWidget()  # Creamos un widget contenedor
        container.setLayout(layout)  # Establecemos el layout como contenido del widget contenedor
        self.setCentralWidget(container)  # Establecemos el widget contenedor como el widget central de la ventana

    def saludar(self):
        nombre = self.nombreInput.text()  # Obtenemos el texto del campo de entrada
        saludo = f"Hola, {nombre}!"  # Creamos el mensaje de saludo
        self.textoLabel.setText(saludo)  # Actualizamos el texto del label con el mensaje de saludo
        self.nombreInput.setDisabled(True) # Deshabilitar volver a escribir una vez se pulsa el botón
        self.botonSaludar.hide() # Esconder el botón cuando se pulsa

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Creamos la aplicación
    window = MainWindow()  # Creamos la ventana principal
    window.show()  # Mostramos la ventana principal
    sys.exit(app.exec())  # Ejecutamos el bucle de eventos de la aplicación