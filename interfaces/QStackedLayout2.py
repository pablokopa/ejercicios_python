import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout, QVBoxLayout, QHBoxLayout, QRadioButton, \
    QCheckBox, QPushButton, QComboBox
from _CaixaCor import CaixaColor

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Colores")  # Establecer el título de la ventana
        self.setMinimumSize(500, 500)  # Establecer el tamaño mínimo de la ventana

        cajaVertical = QVBoxLayout()  # Crear un layout vertical
        self.stack = QStackedLayout()  # Crear un layout apilado

        # Colores Base
        self.stack.addWidget(CaixaColor("red")) # 0
        self.stack.addWidget(CaixaColor("blue")) # 1
        self.stack.addWidget(CaixaColor("green")) # 2
        self.stack.addWidget(CaixaColor("orange")) # 3

        # Colores mezclados
        self.stack.addWidget(CaixaColor("#3152b7")) # 4
        self.stack.addWidget(CaixaColor("#955f20")) # 5
        self.stack.addWidget(CaixaColor("#008080")) # 6
        self.stack.addWidget(CaixaColor("olive")) # 7
        self.stack.addWidget(CaixaColor("brown")) # 8
        self.stack.addWidget(CaixaColor("#ff4000")) # 9
        self.stack.addWidget(CaixaColor("grey"))  # 10
        self.stack.setCurrentIndex(10)  # Establecer el widget gris como el predeterminado

        cajaVertical.addLayout(self.stack)  # Añadir el layout apilado al layout vertical

        # Layouts horizontales (cada fila)
        cajaHorizontal0 = QHBoxLayout()  # Crear un layout horizontal 0
        cajaHorizontal1 = QHBoxLayout()  # Crear un layout horizontal 1
        cajaHorizontal2 = QHBoxLayout()  # Crear un layout horizontal 2
        cajaVertical.addLayout(cajaHorizontal0)  # Añadir el layout horizontal 0 al layout vertical
        cajaVertical.addLayout(cajaHorizontal1)  # Añadir el layout horizontal 1 al layout vertical
        cajaVertical.addLayout(cajaHorizontal2)  # Añadir el layout horizontal 2 al layout vertical

# BOTONES CUADRADOS
        botonCuadradoRojo = QPushButton("Rojo")  # Crear un botón cuadrado con el texto "Rojo"
        cajaHorizontal0.addWidget(botonCuadradoRojo)  # Añadir el botón al layout horizontal
        botonCuadradoRojo.pressed.connect(self.on_boton_rojo)  # Conectar la señal pressed del botón a la función on_Boton_Rojo

        botonCuadradoAzul = QPushButton("Azul")
        cajaHorizontal0.addWidget(botonCuadradoAzul)
        botonCuadradoAzul.pressed.connect(self.on_boton_azul)

        botonCuadradoVerde = QPushButton("Verde")
        cajaHorizontal0.addWidget(botonCuadradoVerde)
        botonCuadradoVerde.pressed.connect(self.on_boton_verde)

        botonCuadradoNaranja = QPushButton("Naranja")
        cajaHorizontal0.addWidget(botonCuadradoNaranja)
        botonCuadradoNaranja.pressed.connect(self.on_boton_naranja)

# BOTONES REDONDOS
        botonRojo = QRadioButton("Rojo")
        cajaHorizontal1.addWidget(botonRojo)
        botonRojo.pressed.connect(self.on_boton_rojo)

        botonAzul = QRadioButton("Azul")
        cajaHorizontal1.addWidget(botonAzul)
        botonAzul.pressed.connect(self.on_boton_azul)

        botonVerde = QRadioButton("Verde")
        cajaHorizontal1.addWidget(botonVerde)
        botonVerde.pressed.connect(self.on_boton_verde)

        botonNaranja = QRadioButton("Naranja")
        cajaHorizontal1.addWidget(botonNaranja)
        botonNaranja.pressed.connect(self.on_boton_naranja)

# BOTONES CHECKBOX
        self.checkRojo = QCheckBox("Rojo")
        cajaHorizontal2.addWidget(self.checkRojo)
        self.checkRojo.clicked.connect(self.chk_rojo_clicked)

        self.checkAzul = QCheckBox("Azul")
        cajaHorizontal2.addWidget(self.checkAzul)
        self.checkAzul.clicked.connect(self.chk_azul_clicked)

        self.checkVerde = QCheckBox("Verde")
        cajaHorizontal2.addWidget(self.checkVerde)
        self.checkVerde.clicked.connect(self.chk_verde_clicked)

        self.checkNaranja = QCheckBox("Naranja")
        cajaHorizontal2.addWidget(self.checkNaranja)
        self.checkNaranja.clicked.connect(self.chk_naranja_clicked)

# COMBOBOX
        cmbCores = QComboBox()
        cmbCores.addItems(("Rojo", "Azul", "Verde", "Naranja"))
        cmbCores.setCurrentIndex(0)
        cmbCores.currentIndexChanged.connect(self.on_cmb_cores_current_index_changed)
        cajaVertical.addWidget(cmbCores)

        contenedor = QWidget()  # Crear un widget contenedor
        contenedor.setLayout(cajaVertical)  # Establecer el layout vertical como el layout del contenedor
        self.setCentralWidget(contenedor)  # Establecer el contenedor como el widget central de la ventana
        self.show()  # Mostrar la ventana

    def on_boton_rojo(self):
        self.stack.setCurrentIndex(0)  # Cambiar al widget rojo

    def on_boton_azul(self):
        self.stack.setCurrentIndex(1)  # Cambiar al widget azul

    def on_boton_verde(self):
        self.stack.setCurrentIndex(2)  # Cambiar al widget verde

    def on_boton_naranja(self):
        self.stack.setCurrentIndex(3)  # Cambiar al widget naranja

    def chk_rojo_clicked(self):
        self.update_checkboxes()
        if self.checkVerde.isChecked():
            self.stack.setCurrentIndex(8)  # Marron
        elif self.checkAzul.isChecked():
            self.stack.setCurrentIndex(4)  # Violeta
        elif self.checkNaranja.isChecked():
            self.stack.setCurrentIndex(9)  # Rojonaranja

    def chk_azul_clicked(self):
        self.update_checkboxes()
        if self.checkVerde.isChecked():
            self.stack.setCurrentIndex(6)  # Azuloso
        elif self.checkRojo.isChecked():
            self.stack.setCurrentIndex(4)  # Violeta
        elif self.checkNaranja.isChecked():
            self.stack.setCurrentIndex(5)  # Violetaclaro

    def chk_verde_clicked(self):
        self.update_checkboxes()
        if self.checkRojo.isChecked():
            self.stack.setCurrentIndex(8)  # Verdemarron
        elif self.checkAzul.isChecked():
            self.stack.setCurrentIndex(6)  # Azuloso
        elif self.checkNaranja.isChecked():
            self.stack.setCurrentIndex(7)  # Verdenaranja

    def chk_naranja_clicked(self):
        self.update_checkboxes()
        if self.checkVerde.isChecked():
            self.stack.setCurrentIndex(7)  # Verdenaranja
        elif self.checkRojo.isChecked():
            self.stack.setCurrentIndex(9)  # Naranjafuerte
        elif self.checkAzul.isChecked():
            self.stack.setCurrentIndex(5)  # Violetaclaro

    # Cambiar colores del combo box
    def on_cmb_cores_current_index_changed(self, indice):
        self.stack.setCurrentIndex(indice)

    # Para que solo se puedan seleccionar 2 checkbox a la vez
    def update_checkboxes(self):
        checkboxes = [self.checkRojo, self.checkAzul, self.checkVerde, self.checkNaranja]
        checked_count = sum(1 for cb in checkboxes if cb.isChecked())
        for cb in checkboxes:
            if not cb.isChecked():
                cb.setEnabled(checked_count < 2)

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Crear la aplicación
    window = VentanaPrincipal()  # Crear la ventana principal
    app.exec()