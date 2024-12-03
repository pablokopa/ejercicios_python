import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTableView, QPushButton, QLineEdit, QWidget, \
    QHBoxLayout, QComboBox, QCheckBox

from ModeloTabla import ModeloTabla

class EjemploQTableView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo QTableView")  # Establecer el título de la ventana
        self.setFixedSize(431, 300)  # Establecer el tamaño fijo de la ventana

        # Datos de ejemplo para la tabla
        self.datos = [['Pedro Piñeiro', '23749103Q', 'Otros', True],
                      ['Keyla Iglesias', '33241349P', 'Mujer', False],
                      ['Pablo Iglesias', '14857729D', 'Hombre', False],
                      ['Sergio Sanroman', '19238894G', 'Otros', False],
                      ['Enrique Fernandez', '92476623K', 'Hombre', True],
                      ['Angel Piñeiro', '27583392H', 'Hombre', True]
        ]

        cajaVertical = QVBoxLayout()  # Crear un layout vertical
        self.tvwTaboa = QTableView()  # Crear un QTableView
        modelo = ModeloTabla(self.datos)  # Crear el modelo de la tabla con los datos
        self.tvwTaboa.setModel(modelo)  # Establecer el modelo en el QTableView
        self.tvwTaboa.setSelectionMode(QTableView.SelectionMode.SingleSelection)  # Establecer el modo de selección

        # Configurarlo para que se pueda seleccionar la tabla y se modifiquen los elementos de abajo
        self.tvwTaboa.selectionModel().selectionChanged.connect(self.seleccion)

        cajaVertical.addWidget(self.tvwTaboa)  # Añadir el QTableView al layout vertical

        cajaHorizontal = QHBoxLayout()  # Crear un layout horizontal
        cajaVertical.addLayout(cajaHorizontal)  # Añadir el layout horizontal al layout vertical

        self.txtNombre = QLineEdit()  # Crear un campo de texto para el nombre
        cajaHorizontal.addWidget(self.txtNombre)  # Añadir el campo de texto al layout horizontal

        self.txtDni = QLineEdit()  # Crear un campo de texto para el DNI
        cajaHorizontal.addWidget(self.txtDni)  # Añadir el campo de texto al layout horizontal

        self.cmbGenero = QComboBox()  # Crear un combo box para el género
        self.cmbGenero.addItems(('Hombre', 'Mujer', 'Otros'))  # Añadir elementos al combo box
        cajaHorizontal.addWidget(self.cmbGenero)  # Añadir el combo box al layout horizontal

        self.chkFallecido = QCheckBox('Fallecido')  # Crear un checkbox para el estado de fallecido
        cajaHorizontal.addWidget(self.chkFallecido)  # Añadir el checkbox al layout horizontal

        contenedor = QWidget()  # Crear un widget contenedor
        contenedor.setLayout(cajaVertical)  # Establecer el layout vertical en el contenedor
        self.setCentralWidget(contenedor)  # Establecer el contenedor como el widget central de la ventana
        self.show()  # Mostrar la ventana

    def seleccion (self):
        index = self.tvwTaboa.selectedIndexes()
        if index:
            fila = index[0].row()
            self.txtNombre.setText(self.datos[fila][0])
            self.txtDni.setText(self.datos[fila][1])
            self.cmbGenero.setCurrentText(self.datos[fila][2])
            self.chkFallecido.setChecked(self.datos[fila][3])

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)  # Crear la aplicación
    ventana = EjemploQTableView()  # Crear la ventana principal
    aplicacion.exec()  # Ejecutar el bucle de eventos de la aplicación