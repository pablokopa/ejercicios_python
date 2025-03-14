import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Definición de la clase VentanaPrincipal que hereda de Gtk.Window
class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        # Configuración del título y tamaño de la ventana
        self.set_title("Ventana Notebook")
        self.set_default_size(600, 600)

        # Creación de un Notebook (carpeta) para contener las páginas
        carpeta = Gtk.Notebook()

        # Creación de la primera página y adición al Notebook
        pagina1 = Gtk.Box()
        pagina1.set_border_width(10)
        pagina1.add(Gtk.Label(label="Página 1"))
        carpeta.append_page(pagina1, Gtk.Label("Página 1"))

        # Creación de la segunda página y adición al Notebook
        pagina2 = Gtk.Box()
        pagina2.set_border_width(10)
        pagina2.add(Gtk.Label(label="Página 2"))
        carpeta.append_page(pagina2, Gtk.Image.new_from_icon_name("help-about", Gtk.IconSize.MENU))

        # Adición del Notebook a la ventana principal
        self.add(carpeta)
        # Conexión del evento de cierre de la ventana con la función Gtk.main_quit
        self.connect("delete-event", Gtk.main_quit)
        # Mostrar todos los widgets
        self.show_all()

# Creación de una instancia de VentanaPrincipal y ejecución del loop principal de GTK
if __name__ == "__main__":
    win = VentanaPrincipal()
    Gtk.main()