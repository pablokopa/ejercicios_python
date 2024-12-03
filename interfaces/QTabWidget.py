import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow, QTabWidget
from _CaixaCor import CaixaColor


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo Stacked Layout")  # Establecer el título de la ventana
        self.setMinimumSize(400, 400)  # Establecer el tamaño mínimo de la ventana

        cajaTabWidget = QTabWidget()  # Crear un layout vertical

        # Tabs de cada color
        cajaTabWidget.addTab(CaixaColor("red"), "Rojo")
        cajaTabWidget.addTab(CaixaColor("blue"), "Azul")
        cajaTabWidget.addTab(CaixaColor("green"), "Verde")
        cajaTabWidget.addTab(CaixaColor("gold"), "Amarillo")
        cajaTabWidget.addTab(CaixaColor("orange"), "Naranja")
        cajaTabWidget.addTab(CaixaColor("purple"), "Morado")
        cajaTabWidget.setMovable(True) # Indica que las pestañas se pueden mover y arrastrar

        cajaTabWidget.setTabPosition(QTabWidget.TabPosition.South) # Colocar los tabs en la parte de abajo

        layout = QVBoxLayout() # Crear layout vertical
        layout.addWidget(cajaTabWidget) # Añadir TabWidget al layout vertical

        contenedor = QWidget()  # Crear un widget contenedor
        contenedor.setLayout(layout)  # Establecer el layout vertical como el layout del contenedor
        self.setCentralWidget(contenedor)  # Establecer el contenedor como el widget central de la ventana
        self.show()  # Mostrar la ventana

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Crear la aplicación
    window = VentanaPrincipal()  # Crear la ventana principal
    app.exec()