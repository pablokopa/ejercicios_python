import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout, QVBoxLayout, QHBoxLayout, QPushButton, \
    QRadioButton, QButtonGroup, QCheckBox
from _CaixaCor import CaixaColor

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo Stacked Layout")  # Establecer el título de la ventana
        self.setMinimumSize(400, 400)  # Establecer el tamaño mínimo de la ventana

        cajaVertical = QVBoxLayout()  # Crear un layout vertical

        self.stack = QStackedLayout()  # Crear un layout apilado
        self.stack.addWidget(CaixaColor("red"))  # Añadir un widget rojo
        self.stack.addWidget(CaixaColor("blue"))  # Añadir un widget azul
        self.stack.addWidget(CaixaColor("green"))  # Añadir un widget verde
        self.stack.addWidget(CaixaColor("orange"))  # Añadir un widget naranja
        self.stack.setCurrentIndex(0)  # Establecer el widget rojo como el predeterminado

        cajaVertical.addLayout(self.stack)  # Añadir el layout apilado al layout vertical

        # Layouts horizontales (cada fila)
        cajaHorizontal1 = QHBoxLayout()  # Crear un layout horizontal 1
        cajaHorizontal2 = QHBoxLayout()  # Crear un layout horizontal 2
        cajaVertical.addLayout(cajaHorizontal1)  # Añadir el layout horizontal 1 al layout vertical
        cajaVertical.addLayout(cajaHorizontal2)  # Añadir el layout horizontal 2 al layout vertical

# BOTONES REDONDOS
        # Botón Rojo
        botonRojo = QRadioButton("Rojo")  # Crear un botón con el texto "Rojo"
        cajaHorizontal1.addWidget(botonRojo)  # Añadir el botón al layout horizontal
        botonRojo.pressed.connect(self.on_Boton_Rojo)  # Conectar la señal pressed del botón a la función on_Boton_Rojo

        # Botón Azul
        botonAzul = QRadioButton("Azul")
        cajaHorizontal1.addWidget(botonAzul)
        botonAzul.pressed.connect(self.on_Boton_Azul)

        # Botón Verde
        botonVerde = QRadioButton("Verde")
        cajaHorizontal1.addWidget(botonVerde)
        botonVerde.pressed.connect(self.on_Boton_Verde)

        # Botón Naranja
        botonNaranja = QRadioButton("Naranja")
        cajaHorizontal1.addWidget(botonNaranja)
        botonNaranja.pressed.connect(self.on_Boton_Naranja)

# BOTONES CHECKBOX
        # Botón Rojo
        checkRojo = QCheckBox("Rojo")  # Crear un botón con el texto "Rojo"
        cajaHorizontal2.addWidget(checkRojo)  # Añadir el botón al layout horizontal
        checkRojo.pressed.connect(self.on_Boton_Rojo)  # Conectar la señal pressed del botón a la función on_Boton_Rojo

        # Botón Azul
        checkAzul = QCheckBox("Azul")
        cajaHorizontal2.addWidget(checkAzul)
        checkAzul.pressed.connect(self.on_Boton_Azul)

        # Botón Verde
        checkVerde = QCheckBox("Verde")
        cajaHorizontal2.addWidget(checkVerde)
        checkVerde.pressed.connect(self.on_Boton_Verde)

        # Botón Naranja
        checkNaranja = QCheckBox("Naranja")
        cajaHorizontal2.addWidget(checkNaranja)
        checkNaranja.pressed.connect(self.on_Boton_Naranja)

        contenedor = QWidget()  # Crear un widget contenedor
        contenedor.setLayout(cajaVertical)  # Establecer el layout vertical como el layout del contenedor
        self.setCentralWidget(contenedor)  # Establecer el contenedor como el widget central de la ventana
        self.show()  # Mostrar la ventana

    def on_Boton_Rojo(self):
        self.stack.setCurrentIndex(0)  # Cambiar al widget rojo

    def on_Boton_Azul(self):
        self.stack.setCurrentIndex(1)  # Cambiar al widget azul

    def on_Boton_Verde(self):
        self.stack.setCurrentIndex(2)  # Cambiar al widget verde

    def on_Boton_Naranja(self):
        self.stack.setCurrentIndex(3)  # Cambiar al widget naranja

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Crear la aplicación
    window = VentanaPrincipal()  # Crear la ventana principal
    app.exec()