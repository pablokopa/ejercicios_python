import sqlite3 as dbapi

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo con Gtk TreeView filtrado e ordenado")

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.filtradoXenero = None
        modelo = Gtk.ListStore(str, str, int, str)

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

        tryDatosUsuarios = Gtk.TreeView(model=modelo)
        seleccion = tryDatosUsuarios.get_selection()

        for i, tituloColumna in enumerate(["DNI", "Nome", "Edade"]):
            if tituloColumna == "Edade":
                celda = Gtk.CellRendererProgress()
                columna = Gtk.TreeViewColumn(tituloColumna, celda, value=i)
            else:
                celda = Gtk.CellRendererText()
                columna = Gtk.TreeViewColumn(tituloColumna, celda, text=i)
            tryDatosUsuarios.append_column(columna)

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

        caixaV.pack_start(tryDatosUsuarios, True, True, 0)
        self.add(caixaV)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_celdaXenero_edited(self, celda, fila, texto, modelo, columna):
        modelo[fila][columna] = texto

if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()