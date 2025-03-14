import gi

gi.require_version("Gtk", "3.0")
from gi.repository.Gtk import TreeStore
from gi.repository import Gtk
import sqlite3 as dbapi


# Definición de la clase FiestraPrincipal que hereda de Gtk.Window
class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        # Configuración del título de la ventana
        self.set_title("Exemplo Gtk TreeView en arbore")

        # Creación de una caja vertical para contener los widgets
        cajaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Creación del modelo de datos TreeStore
        modelo = TreeStore(str, int)

        # Añadir datos al modelo en una estructura de árbol
        for avo in range(5):
            punteiroAvo = modelo.append(None, ["Avo %i" % (avo,), avo])
            for pai in range(4):
                punteiroPai = modelo.append(punteiroAvo, ["Pai %i do avo %i" % (pai, avo), pai])
                for fillo in range(3):
                    modelo.append(punteiroPai, ["Neto %i do pai %i do avo %i" % (fillo, pai, avo), fillo])

        # Creación del TreeView y configuración de las columnas
        tryVista = Gtk.TreeView(model=modelo)

        # Creación de la primera columna del TreeView
        tryColumna = Gtk.TreeViewColumn("Parentesco")
        tryVista.append_column(tryColumna)
        celda = Gtk.CellRendererText()
        tryColumna.pack_start(celda, True)
        tryColumna.add_attribute(celda, "text", 0)

        # Creación de la segunda columna del TreeView
        tryColumna = Gtk.TreeViewColumn("Orde")
        tryVista.append_column(tryColumna)
        celda = Gtk.CellRendererText()
        tryColumna.pack_start(celda, True)
        tryColumna.add_attribute(celda, "text", 1)

        # Añadir el TreeView a la caja
        cajaV.pack_start(tryVista, True, True, 0)

        # Añadir la caja a la ventana principal
        self.add(cajaV)
        # Conexión del evento de cierre de la ventana con la función Gtk.main_quit
        self.connect("delete-event", Gtk.main_quit)
        # Mostrar todos los widgets
        self.show_all()


# Creación de una instancia de FiestraPrincipal y ejecución del loop principal de GTK
if __name__ == "__main__":
    fiestra = FiestraPrincipal()
    fiestra.show_all()
    Gtk.main()