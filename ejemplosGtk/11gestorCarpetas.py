import gi
gi.require_version("Gtk", "3.0")
from gi.repository.Gtk import TreeStore
from gi.repository import Gtk, GdkPixbuf
import os

class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Explorador de Directorios con Gtk TreeView")
        self.set_default_size(600, 400)

        cajaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Crear el modelo TreeStore para almacenar los directorios
        modelo = TreeStore(GdkPixbuf.Pixbuf, str)

        # Cargar iconos
        icono_carpeta = Gtk.IconTheme.get_default().load_icon("folder", 16, 0)
        icono_documento = Gtk.IconTheme.get_default().load_icon("text-x-generic", 16, 0)

        # Función para añadir directorios al modelo con un límite de profundidad
        def agregar_directorios(padre, ruta, profundidad, max_profundidad=5):
            if profundidad > max_profundidad:
                return
            try:
                for nombre in os.listdir(ruta):
                    if nombre.startswith('.'):
                        continue  # Omitir directorios ocultos
                    ruta_completa = os.path.join(ruta, nombre)
                    if os.path.isdir(ruta_completa) and not os.path.islink(ruta_completa):
                        punteiro = modelo.append(padre, [icono_carpeta, nombre])
                        agregar_directorios(punteiro, ruta_completa, profundidad + 1)
                    else:
                        modelo.append(padre, [icono_documento, nombre])
            except PermissionError:
                pass

        # Añadir el directorio raíz al modelo
        agregar_directorios(None, "/home/dam/DAM", 0)

        # Crear el TreeView y añadir las columnas
        tryVista = Gtk.TreeView(model=modelo)
        tryColumna = Gtk.TreeViewColumn("Icono")
        tryVista.append_column(tryColumna)
        celda_icono = Gtk.CellRendererPixbuf()
        tryColumna.pack_start(celda_icono, False)
        tryColumna.add_attribute(celda_icono, "pixbuf", 0)

        tryColumna = Gtk.TreeViewColumn("Directorios")
        tryVista.append_column(tryColumna)
        celda_texto = Gtk.CellRendererText()
        tryColumna.pack_start(celda_texto, True)
        tryColumna.add_attribute(celda_texto, "text", 1)

        cajaV.pack_start(tryVista, True, True, 0)

        self.add(cajaV)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    fiestra = FiestraPrincipal()
    Gtk.main()