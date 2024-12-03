import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QListView, QTabWidget, QWidget, QPushButton, QLineEdit
from ModeloTareas import ModeloTareas

from PyQt6.QtGui import QPalette, QColor

class EjemploQListView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo QListView")  # Título de la ventana
        self.setMinimumSize(200, 300) # Tamaño minimo de la ventana

        # Cambiar el color de fondo
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("lightgrey"))
        self.setPalette(paleta)

        listaTareas = [(False, 'Ir al gimnasio'), (True, 'Hacer la compra')]  # Lista de tareas
        self.modelo = ModeloTareas(listaTareas)  # Crear el modelo con la lista de tareas

        cajaV = QVBoxLayout()  # Layout vertical

        # QList
        self.lstTareas = QListView()  # Crear QListView
        self.lstTareas.setModel(self.modelo)  # Establecer el modelo en el QListView
        self.lstTareas.setSelectionMode(QListView.SelectionMode.MultiSelection) # Permitir multiselección
        cajaV.addWidget(self.lstTareas)  # Añadir el QListView al layout vertical

        # Botones Superiores
        cajaHBotones = QHBoxLayout()

        botonDelete = QPushButton("Eliminar")
        botonDelete.pressed.connect(self.on_boton_delete_pressed)
        cajaHBotones.addWidget(botonDelete)

        botonComplete = QPushButton("Completar")
        botonComplete.pressed.connect(self.on_boton_complete_pressed)
        cajaHBotones.addWidget(botonComplete)

        cajaV.addLayout(cajaHBotones)

        # TextField
        self.textoTarea = QLineEdit()
        cajaV.addWidget(self.textoTarea)

        # Botón Inferior
        botonAddTarea = QPushButton("Añadir Tarea")
        botonAddTarea.pressed.connect(self.on_boton_add_tarea_pressed)
        cajaV.addWidget(botonAddTarea)

        # Crear Ventana
        contenedor = QWidget()  # Widget contenedor
        contenedor.setLayout(cajaV)  # Establer el layout en el contenedor
        tabWidget = QTabWidget()  # Crear un QTabWidget
        tabWidget.addTab(contenedor, "Tareas")  # Añadir el contenedor como una pestaña
        self.setCentralWidget(tabWidget)  # Establer el QTabWidget como el widget central

# FUNCIONES
    # Función para dar funcionalidad al botón eliminar
    def on_boton_delete_pressed(self):
        indices = self.lstTareas.selectedIndexes() # Obtener los índices seleccionados
        # Verificar si hay índices seleccionados
        if indices:
            # Extraer los índices de fila y eliminar las tareas
            for indice in sorted(indices, reverse=True):
                del self.modelo.tareas[indice.row()]
            self.modelo.layoutChanged.emit() # Emitir señal para notificar que el modelo ha cambiado
            self.lstTareas.clearSelection()

    # Función para dar funcionalidad al botón completar
    def on_boton_complete_pressed(self):
        indices = self.lstTareas.selectedIndexes()
        if indices:
            for indice in indices:
                _ , texto = self.modelo.tareas [indice.row()]
                self.modelo.tareas [indice.row()] = (True, texto)
                self.modelo.dataChanged.emit(indice, indice)
            self.lstTareas.clearSelection()

    # Función para dar funcionalidad al botón añadir tarea
    def on_boton_add_tarea_pressed(self):
        texto = self.textoTarea.text().strip() # Obtener texto del textField y eliminar espacios en blanco al inicio y al final
        # Verificar si el texto no está vacío
        if texto:
            self.modelo.tareas.append((False, texto)) # Añadir la nueva tarea a la lista de tareas del modelo
            self.modelo.layoutChanged.emit()
            self.textoTarea.setText('') # Limpiar el campo de entrada de texto

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EjemploQListView()
    window.show()
    app.exec()