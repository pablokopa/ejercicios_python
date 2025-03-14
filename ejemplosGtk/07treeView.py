import sqlite3 as dbapi

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo con Gtk TreeView")

        columnas = ["Nombre", "Apellido", "Número de teléfono"]
        agenda_telefonica = [["Pepe", "Pérez", "986543210"],
                             ["María", "López", "986123456"],
                             ["Manuel", "García", "986654321"],
                             ["Ramón", "Fernández", "986234567"]]
        listin = Gtk.ListStore(str, str, str)

        for contacto in agenda_telefonica:
            listin.append(contacto)

        try:
            bbdd = dbapi.connect("bdListinTelefonico.dat")
            cursor = bbdd.cursor()
            cursor.execute ("SELECT * FROM listaTelefonos")
            for usuarioListin in cursor:
                axendaTelefonica.append(usuarioListin)
            cursor.close()
            bbdd.close()
        except sqlite3.DatabaseError as e:
            print("Error en base de datos: " + str(e))
        except Exception as e:
            print("Error: " + str(e))

        caja_v = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        vista = Gtk.TreeView(model=listin)
        obxectoSelecion = vista.get_selection()
        obxectoSelecion.connect("changed", self.on_obxectoSeleccion_changed)
        for i in range(len(columnas)):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(columnas[i], celda, text=i)
            vista.append_column(columna)  # Añadir la columna al TreeView

        caja_v.pack_start(vista, True, True, 0)  # Añadir el TreeView a la caja

        self.add(caja_v)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_obxectoSeleccion_changed(self, seleccion):
        (modelo, fila) = seleccion.get_selected()
        print(modelo [fila][0], " ", modelo [fila][1], " ", modelo [fila][2])

if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()