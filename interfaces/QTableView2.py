import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTableView, QPushButton, QLineEdit, QWidget, \
    QHBoxLayout, QComboBox, QCheckBox

from ModeloTabla import ModeloTabla

class EjemploQTableView2(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo QTableView")  # Establecer el título de la ventana
        self.setFixedSize(431, 600)  # Establecer el tamaño fijo de la ventana

        # Datos de ejemplo para la tabla
        self.datos = [['Pedro Piñeiro', '23749103Q', 'Otros', True],
                      ['Keyla Iglesias', '33241349P', 'Mujer', False],
                      ['Pablo Iglesias', '14857729D', 'Hombre', False],
                      ['Sergio Sanroman', '19238894G', 'Otros', False],
                      ['Enrique Fernandez', '92476623K', 'Hombre', True],
                      ['Angel Piñeiro', '27583392H', 'Hombre', True]
        ]

        cajaVertical = QVBoxLayout()  # Crear un layout vertical
        self.tvwTabla = QTableView()  # Crear un QTableView
        modelo = ModeloTabla(self.datos)  # Crear el modelo de la tabla con los datos
        self.tvwTabla.setModel(modelo)  # Establecer el modelo en el QTableView
        self.tvwTabla.setSelectionMode(QTableView.SelectionMode.SingleSelection)  # Establecer el modo de selección

        # Configurarlo para que se pueda seleccionar la tabla y se modifiquen los elementos de abajo
        self.tvwTabla.selectionModel().selectionChanged.connect(self.seleccion)

        cajaVertical.addWidget(self.tvwTabla)  # Añadir el QTableView al layout vertical

# Añadir campos de nombre, dni, genero y fallecido
        cajaHorizontal = QHBoxLayout()  # Crear un layout horizontal
        cajaVertical.addLayout(cajaHorizontal)  # Añadir el layout horizontal al layout vertical

        self.txtNombre = QLineEdit()  # Crear un campo de texto para el nombre
        self.txtNombre.setPlaceholderText("Nombre")
        cajaHorizontal.addWidget(self.txtNombre)  # Añadir el campo de texto al layout horizontal

        self.txtDni = QLineEdit()  # Crear un campo de texto para el DNI
        self.txtDni.setPlaceholderText("DNI")
        cajaHorizontal.addWidget(self.txtDni)  # Añadir el campo de texto al layout horizontal

        self.cmbGenero = QComboBox()  # Crear un combo box para el género
        self.cmbGenero.addItems(('Hombre', 'Mujer', 'Otros'))  # Añadir elementos al combo box
        self.cmbGenero.setCurrentText('')
        cajaHorizontal.addWidget(self.cmbGenero)  # Añadir el combo box al layout horizontal

        self.chkFallecido = QCheckBox('Fallecido')  # Crear un checkbox para el estado de fallecido
        cajaHorizontal.addWidget(self.chkFallecido)  # Añadir el checkbox al layout horizontal

# Añadir botones de aceptar, editar y eliminar
        cajaHorizontal2 = QHBoxLayout()
        cajaHorizontal3 = QHBoxLayout()
        cajaHorizontal4 = QHBoxLayout()
        cajaVertical.addLayout(cajaHorizontal2)
        cajaVertical.addLayout(cajaHorizontal3)
        cajaVertical.addLayout(cajaHorizontal4)

        botonEditar = QPushButton("Editar") # Crea botón editar
        botonEditar.pressed.connect(self.editar)
        cajaHorizontal2.addWidget(botonEditar)

        botonCancelar = QPushButton("Cancelar") # Crea botón eliminar
        botonCancelar.pressed.connect(self.cancelar)
        cajaHorizontal2.addWidget(botonCancelar)

        botonEliminar = QPushButton("Añadir")  # Crea botón añadir
        botonEliminar.pressed.connect(self.anadir)
        cajaHorizontal3.addWidget(botonEliminar)

        botonEliminar = QPushButton("Eliminar")  # Crea botón eliminar
        botonEliminar.pressed.connect(self.eliminar)
        cajaHorizontal4.addWidget(botonEliminar)

        contenedor = QWidget()  # Crear un widget contenedor
        contenedor.setLayout(cajaVertical)  # Establecer el layout vertical en el contenedor
        self.setCentralWidget(contenedor)  # Establecer el contenedor como el widget central de la ventana
        self.show()  # Mostrar la ventana

    def seleccion (self):
        index = self.tvwTabla.selectedIndexes()
        if index:
            fila = index[0].row()
            self.txtNombre.setText(self.datos[fila][0])
            self.txtDni.setText(self.datos[fila][1])
            self.cmbGenero.setCurrentText(self.datos[fila][2])
            self.chkFallecido.setChecked(self.datos[fila][3])

    def cancelar(self):
        self.txtNombre.clear()
        self.txtDni.clear()
        self.cmbGenero.setCurrentText('')
        self.chkFallecido.setChecked(False)

    def editar(self):
        indice = self.tvwTabla.selectedIndexes()
        if indice:
            if self.txtNombre.text() == '' or self.txtDni.text() == '' or self.cmbGenero.currentIndex() == -1:
                print("Faltan datos")
            else:
                fila = indice[0].row()
                self.datos[fila][0] = self.txtNombre.text()
                self.datos[fila][1] = self.txtDni.text()
                self.datos[fila][2] = self.cmbGenero.currentText()
                self.datos[fila][3] = self.chkFallecido.isChecked()
                self.tvwTabla.model().layoutChanged.emit()
                self.txtNombre.clear()
                self.txtDni.clear()
                self.cmbGenero.setCurrentText('')
                self.chkFallecido.setChecked(False)

    def anadir(self):
        if self.txtNombre.text() == '' or self.txtDni.text() == '' or self.cmbGenero.currentIndex() == -1:
            print("Faltan datos")
        else:
            self.datos.append([self.txtNombre.text(), self.txtDni.text(), self.cmbGenero.currentText(), self.chkFallecido.isChecked()])
            self.tvwTabla.model().layoutChanged.emit()
            self.txtNombre.clear()
            self.txtDni.clear()
            self.cmbGenero.setCurrentText('')
            self.chkFallecido.setChecked(False)

    def eliminar(self):
        if self.txtNombre.text() == '' or self.txtDni.text() == '' or self.cmbGenero.currentIndex() == -1:
            print("Faltan datos")
        else:
            self.datos.remove([self.txtNombre.text(), self.txtDni.text(), self.cmbGenero.currentText(), self.chkFallecido.isChecked()])
            self.tvwTabla.model().layoutChanged.emit()
            self.txtNombre.clear()
            self.txtDni.clear()
            self.cmbGenero.setCurrentText('')
            self.chkFallecido.setChecked(False)

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)  # Crear la aplicación
    ventana = EjemploQTableView2()  # Crear la ventana principal
    aplicacion.exec()  # Ejecutar el bucle de eventos de la aplicación