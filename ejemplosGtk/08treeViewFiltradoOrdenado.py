import sqlite3 as dbapi

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Definición de la clase VentanaPrincipal que hereda de Gtk.Window
class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        # Configuración del título de la ventana
        self.set_title("Exemplo con Gtk TreeView filtrado e ordenado")

        # Creación de una caja vertical para contener los widgets
        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Inicialización del filtro de género
        self.filtradoXenero = None
        # Creación del modelo de datos
        modelo = Gtk.ListStore(str, str, int, str)

        # Conexión a la base de datos y obtención de los datos de los usuarios
        try:
            bbdd = dbapi.connect("baseDatos2.dat")
            cursor = bbdd.cursor()
            cursor.execute("SELECT dni, nome, edade, xenero FROM usuarios")
            for rexistro in cursor:
                modelo.append(rexistro)
        except dbapi.DatabaseError as e:
            print("Error en base de datos: " + str(e))
        finally:
            cursor.close()
            bbdd.close()

        # Creación del TreeView y configuración de la selección
        tryDatosUsuarios = Gtk.TreeView(model=modelo)
        seleccion = tryDatosUsuarios.get_selection()

        # Creación de las columnas del TreeView
        for i, tituloColumna in enumerate(["DNI", "Nome", "Edade"]):
            if tituloColumna == "Edade":
                celda = Gtk.CellRendererProgress()
                columna = Gtk.TreeViewColumn(tituloColumna, celda, value=i)
            else:
                celda = Gtk.CellRendererText()
                columna = Gtk.TreeViewColumn(tituloColumna, celda, text=i)
            tryDatosUsuarios.append_column(columna)

        # Creación del modelo para el ComboBox de género
        modeloCombo = Gtk.ListStore(str)
        modeloCombo.append(("Muller",))
        modeloCombo.append(("Home",))
        modeloCombo.append(("Outros",))
        celda = Gtk.CellRendererCombo()
        celda.set_property("editable", True)
        celda.set_property("model", modeloCombo)
        celda.set_property("text-column", 0)
        celda.set_property("has-entry", False)
        celda.connect("edited", self.on_celdaXenero_edited, modelo, 3)
        columna = Gtk.TreeViewColumn("Xenero", celda, text=3)
        tryDatosUsuarios.append_column(columna)

        # Añadir el TreeView a la caja
        caixaV.pack_start(tryDatosUsuarios, True, True, 0)
        # Añadir la caja a la ventana principal
        self.add(caixaV)
        # Conexión del evento de cierre de la ventana con la función Gtk.main_quit
        self.connect("delete-event", Gtk.main_quit)
        # Mostrar todos los widgets
        self.show_all()

    # Método para manejar la edición de la celda de género
    def on_celdaXenero_edited(self, celda, fila, texto, modelo, columna):
        modelo[fila][columna] = texto

# Creación de una instancia de VentanaPrincipal y ejecución del loop principal de GTK
if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()