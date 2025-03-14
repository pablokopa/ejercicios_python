import gi
gi.require_version("Gtk", "3.0")
from gi.repository.Gtk import TreeStore
from gi.repository import Gtk
import sqlite3 as dbapi

class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo Gtk TreeView en arbore")

        cajaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        modelo = TreeStore(str,int)

        for avo in range(5):
            punteiroAvo = modelo.append(None, ["Avo %i" % (avo,),avo])
            for pai in range(4):
                punteiroPai = modelo.append(punteiroAvo, ["Pai %i do avo %i" % (pai, avo),pai])
                for fillo in range(3):
                    modelo.append(punteiroPai, ["Neto %i do pai %i do avo %i" % (fillo, pai,avo),fillo])

        tryVista = Gtk.TreeView(model=modelo)
        tryColumna = Gtk.TreeViewColumn("Parentesco")
        tryVista.append_column(tryColumna)
        celda = Gtk.CellRendererText()
        tryColumna.pack_start(celda, True)
        tryColumna.add_attribute(celda, "text", 0)

        tryColumna = Gtk.TreeViewColumn("Orde")
        tryVista.append_column(tryColumna)
        celda = Gtk.CellRendererText()
        tryColumna.pack_start(celda, True)
        tryColumna.add_attribute(celda, "text", 1)

        cajaV.pack_start(tryVista, True, True, 0)


        self.add(cajaV)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    fiestra = FiestraPrincipal()
    fiestra.show_all()
    Gtk.main()