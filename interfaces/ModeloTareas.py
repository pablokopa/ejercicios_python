from PyQt6.QtCore import QAbstractListModel, Qt
from PyQt6.QtGui import QImage

# Cargar imágenes para los estados de las tareas
tick = QImage('tick.png')
cross = QImage('cross.png')

class ModeloTareas(QAbstractListModel):
    def __init__(self, tareas=None):
        super().__init__()
        self.tareas = tareas or []  # Inicializar la lista de tareas

    def data(self, indice, rol):
        # Proveer datos para cada rol
        if rol == Qt.ItemDataRole.DisplayRole:
            _, texto = self.tareas[indice.row()]  # Obtener el texto de la tarea
            return texto
        if rol == Qt.ItemDataRole.DecorationRole:
            estado, _ = self.tareas[indice.row()]  # Obtener el estado de la tarea
            if estado:
                return tick  # Devolver imagen de tarea completada
            else:
                return cross  # Devolver imagen de tarea no completada

    def rowCount(self, indice):
        return len(self.tareas)  # Devolver el número de tareas