import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTableView, QPushButton, QLineEdit, QWidget, \
    QHBoxLayout, QComboBox, QCheckBox

from conexionBD import ConexionBD
from ModeloTabla import ModeloTabla
from CrearTablasBD import CrearTablasBD  # Importar la clase CrearTablasBD

class EjemploQTableView2(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo QTableView")  # Establecer el título de la ventana
        self.setFixedSize(850, 350)  # Establecer el tamaño fijo de la ventana

        # Crear una instancia de CrearTablasBD
        self.creaTablas = CrearTablasBD()

        # Recuperar datos de la base de datos
        self.datos = self.creaTablas.consultar_usuarios()

        cajaPrincipal = QHBoxLayout()  # Crear un layout horizontal principal
        cajaVerticalTabla = QVBoxLayout()  # Crear un layout vertical para la tabla
        cajaVerticalControles = QVBoxLayout()  # Crear un layout vertical para los controles

        self.tvwTabla = QTableView()  # Crear un QTableView

        modelo = ModeloTabla(self.datos)  # Crear el modelo de la tabla con los datos recuperados
        self.tvwTabla.setModel(modelo)  # Establecer el modelo en el QTableView
        self.tvwTabla.setSelectionMode(QTableView.SelectionMode.SingleSelection)  # Establecer el modo de selección

        # Configurarlo para que se pueda seleccionar la tabla y se modifiquen los elementos de abajo
        self.tvwTabla.selectionModel().selectionChanged.connect(self.seleccion)

        cajaVerticalTabla.addWidget(self.tvwTabla)  # Añadir el QTableView al layout vertical de la tabla

        # Añadir campos de nombre y genero
        cajaHorizontal1 = QHBoxLayout()  # Crear un layout horizontal
        self.txtNombre = QLineEdit()  # Crear un campo de texto para el nombre
        self.txtNombre.setPlaceholderText("Nombre")
        cajaHorizontal1.addWidget(self.txtNombre)  # Añadir el campo de texto al layout horizontal

        self.cmbGenero = QComboBox()  # Crear un combo box para el género
        self.cmbGenero.addItems(('Hombre', 'Mujer', 'Otros'))  # Añadir elementos al combo box
        self.cmbGenero.setCurrentText('')
        cajaHorizontal1.addWidget(self.cmbGenero)  # Añadir el combo box al layout horizontal

        cajaVerticalControles.addLayout(cajaHorizontal1)  # Añadir el layout horizontal al layout vertical de controles

        # Añadir campos de dni y fallecido
        cajaHorizontal2 = QHBoxLayout()  # Crear un layout horizontal
        self.txtDni = QLineEdit()  # Crear un campo de texto para el DNI
        self.txtDni.setPlaceholderText("DNI")
        cajaHorizontal2.addWidget(self.txtDni)  # Añadir el campo de texto al layout horizontal

        self.chkFallecido = QCheckBox('Fallecido')  # Crear un checkbox para el estado de fallecido
        cajaHorizontal2.addWidget(self.chkFallecido)  # Añadir el checkbox al layout horizontal

        cajaVerticalControles.addLayout(cajaHorizontal2)  # Añadir el layout horizontal al layout vertical de controles

        # Añadir botones de nuevo, modificar y borrar
        cajaHorizontal3 = QHBoxLayout()
        botonNuevo = QPushButton("Nuevo")  # Crea botón nuevo
        botonNuevo.pressed.connect(self.anadir)
        cajaHorizontal3.addWidget(botonNuevo)

        botonModificar = QPushButton("Modificar")  # Crea botón modificar
        botonModificar.pressed.connect(self.editar)
        cajaHorizontal3.addWidget(botonModificar)

        botonBorrar = QPushButton("Borrar")  # Crea botón borrar
        botonBorrar.pressed.connect(self.eliminar)
        cajaHorizontal3.addWidget(botonBorrar)

        cajaVerticalControles.addLayout(cajaHorizontal3)  # Añadir el layout horizontal al layout vertical de controles

        # Añadir botones de aceptar y cancelar
        cajaHorizontal4 = QVBoxLayout()

        self.botonAceptar = QPushButton("Aceptar")  # Crea botón aceptar
        cajaHorizontal4.addWidget(self.botonAceptar)
        self.botonAceptar.setEnabled(False) # Bloquear botón

        self.botonCancelar = QPushButton("Cancelar")  # Crea botón cancelar
        self.botonCancelar.pressed.connect(self.cancelar)
        cajaHorizontal4.addWidget(self.botonCancelar)
        self.botonCancelar.setEnabled(False) # Bloquear botón

        cajaVerticalControles.addLayout(cajaHorizontal4)  # Añadir el layout vertical al layout vertical de controles

        cajaPrincipal.addLayout(cajaVerticalTabla)  # Añadir el layout de la tabla al layout principal
        cajaPrincipal.addLayout(cajaVerticalControles)  # Añadir el layout de controles al layout principal

        contenedor = QWidget()  # Crear un widget contenedor
        contenedor.setLayout(cajaPrincipal)  # Establecer el layout principal en el contenedor
        self.setCentralWidget(contenedor)  # Establecer el contenedor como el widget central de la ventana
        self.show()  # Mostrar la ventana

    def seleccion(self):
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

    def anadir(self):
        if self.txtNombre.text() == '' or self.txtDni.text() == '' or self.cmbGenero.currentIndex() == -1:
            print("Faltan datos")
        else:
            # Insertar nuevo usuario en la base de datos
            self.creaTablas.insertar_usuario(self.txtNombre.text(), self.txtDni.text(), self.cmbGenero.currentText(),
                                             self.chkFallecido.isChecked())
            # Actualizar los datos en la tabla
            self.datos = self.creaTablas.consultar_usuarios()
            self.tvwTabla.setModel(ModeloTabla(self.datos))  # Actualizar el modelo de la tabla
            self.tvwTabla.model().layoutChanged.emit()
            self.txtNombre.clear()
            self.txtDni.clear()
            self.cmbGenero.setCurrentText('')
            self.chkFallecido.setChecked(False)

            # Desbloquear botones aceptar y cancelar cuando se hace click en el boton nuevo
            self.botonAceptar.setEnabled(True)  # Bloquear botón
            self.botonCancelar.setEnabled(True)  # Bloquear botón

    def editar(self):
        indice = self.tvwTabla.selectedIndexes()
        if indice:
            if self.txtNombre.text() == '' or self.txtDni.text() == '' or self.cmbGenero.currentIndex() == -1:
                print("Faltan datos")
            else:
                fila = indice[0].row()
                nombre = self.txtNombre.text()
                dni = self.txtDni.text()
                genero = self.cmbGenero.currentText()
                fallecido = self.chkFallecido.isChecked()
                self.creaTablas.actualizar_usuario(nombre, dni, genero, fallecido)  # Actualizar en la base de datos
                self.datos[fila] = (nombre, dni, genero, fallecido)  # Actualizar los datos en la lista local
                self.tvwTabla.model().layoutChanged.emit()  # Emitir señal de cambio de layout
                self.txtNombre.clear()
                self.txtDni.clear()
                self.cmbGenero.setCurrentText('')
                self.chkFallecido.setChecked(False)

    def eliminar(self):
        indice = self.tvwTabla.selectedIndexes()
        if indice:
            fila = indice[0].row()
            dni = self.datos[fila][1]  # Obtener el DNI del usuario seleccionado
            self.creaTablas.eliminar_usuario(dni)  # Eliminar de la base de datos
            self.datos = self.creaTablas.consultar_usuarios()  # Refrescar los datos
            self.tvwTabla.setModel(ModeloTabla(self.datos))  # Actualizar el modelo de la tabla
            self.tvwTabla.model().layoutChanged.emit()
            self.txtNombre.clear()
            self.txtDni.clear()
            self.cmbGenero.setCurrentText('')
            self.chkFallecido.setChecked(False)

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)  # Crear la aplicación
    ventana = EjemploQTableView2()  # Crear la ventana principal
    aplicacion.exec()  # Ejecutar el bucle de eventos de la aplicación