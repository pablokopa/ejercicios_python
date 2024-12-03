from PyQt6.QtCore import QAbstractTableModel, Qt
from PyQt6.QtGui import QColor, QIcon, QFont

class ModeloTabla(QAbstractTableModel):
    def __init__(self, tabla):
        super().__init__()
        self.tabla = tabla # Almacena los datos de la tabla

    def rowCount(self, indice):
        return len(self.tabla) # Devuelve el número de filas en la tabla

    def columnCount(self, indice):
        return len(self.tabla[0]) if len(self.tabla) != 0 else 0

    def data(self, indice, rol):
        if rol == Qt.ItemDataRole.EditRole or rol == Qt.ItemDataRole.DisplayRole:
            valor = self.tabla[indice.row()][indice.column()]  # Obtiene el valor de la celda
            if indice.column() == 3:  # Columna de "Fallecido"
                return "Fallecido" if valor else "Vivo"
            return valor
        if rol == Qt.ItemDataRole.BackgroundRole:
            if self.tabla[indice.row()][2] == "Hombre":
                return QColor('lightblue') # Color de fondo para "Hombre"
            elif self.tabla[indice.row()][2] == "Mujer":
                return QColor('pink') # Color de fondo para "Mujer"
            elif self.tabla[indice.row()][2] == "Otros":
                return QColor('orange') # Color de fondo para "Otros"
        if rol == Qt.ItemDataRole.ForegroundRole:
            if self.tabla[indice.row()][3] == True:
                if indice.column() == 3:
                    return QColor('red') # Color de texto para "Fallecido"
            elif self.tabla[indice.row()][3] == False:
                if indice.column() == 3:
                    return QColor('green') # Color de texto para "Vivo"

        if rol == Qt.ItemDataRole.DecorationRole:
            if isinstance(self.tabla[indice.row()][indice.column()], bool):
                if self.tabla[indice.row()][indice.column()]:
                    return QIcon('cross.png') # Icono para "Fallecido"
                else:
                    return QIcon('tick.png')  # Icono para "Vivo"

    def headerData(self, seccion, orientacion, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            if orientacion == Qt.Orientation.Horizontal:
                headers = ["Nombre", "DNI", "Genero", "Fallecido"] # Encabezados de las columnas
                return headers[seccion]
        if rol == Qt.ItemDataRole.FontRole:
            if orientacion == Qt.Orientation.Horizontal:
                font = QFont()
                font.setBold(True) # Fuente en negrita para los encabezados
                return font
        return super().headerData(seccion, orientacion, rol)