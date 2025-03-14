import sqlite3 as dbapi

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


# Definición de la clase VentanaPrincipal que hereda de Gtk.Window
class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        # Configuración del título de la ventana
        self.set_title("Exemplo con Gtk TreeView")

        # Definición de las columnas y datos de la agenda telefónica
        columnas = ["Nombre", "Apellido", "Número de teléfono"]
        agenda_telefonica = [["Pepe", "Pérez", "986543210"],
                             ["María", "López", "986123456"],
                             ["Manuel", "García", "986654321"],
                             ["Ramón", "Fernández", "986234567"]]
        listin = Gtk.ListStore(str, str, str)

        # Añadir los contactos a la lista
        for contacto in agenda_telefonica:
            listin.append(contacto)

        # Intentar conectar a la base de datos y obtener datos adicionales
        try:
            bbdd = dbapi.connect("bdListinTelefonico.dat")
            cursor = bbdd.cursor()
            cursor.execute("SELECT * FROM listaTelefonos")
            for usuarioListin in cursor:
                listin.append(usuarioListin)
            cursor.close()
            bbdd.close()
        except dbapi.DatabaseError as e:
            print("Error en base de datos: " + str(e))
        except Exception as e:
            print("Error: " + str(e))

        # Creación de una caja vertical para contener los widgets
        caja_v = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Creación del TreeView y configuración de la selección
        vista = Gtk.TreeView(model=listin)
        obxectoSelecion = vista.get_selection()
        obxectoSelecion.connect("changed", self.on_obxectoSeleccion_changed)

        # Añadir las columnas al TreeView
        for i in range(len(columnas)):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(columnas[i], celda, text=i)
            vista.append_column(columna)

        # Añadir el TreeView a la caja
        caja_v.pack_start(vista, True, True, 0)

        # Añadir la caja a la ventana principal
        self.add(caja_v)
        # Conexión del evento de cierre de la ventana con la función Gtk.main_quit
        self.connect("delete-event", Gtk.main_quit)
        # Mostrar todos los widgets
        self.show_all()

    # Método para manejar el cambio de selección en el TreeView
    def on_obxectoSeleccion_changed(self, seleccion):
        (modelo, fila) = seleccion.get_selected()
        print(modelo[fila][0], " ", modelo[fila][1], " ", modelo[fila][2])


# Creación de una instancia de VentanaPrincipal y ejecución del loop principal de GTK
if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()