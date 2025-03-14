import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ventana Notebook")
        self.set_default_size(600, 600)

        carpeta = Gtk.Notebook()

        pagina1 = Gtk.Box()
        pagina1.set_border_width(10)
        pagina1.add(Gtk.Label(label = "Página 1"))
        carpeta.append_page(pagina1, Gtk.Label("Página 1"))

        pagina2 = Gtk.Box()
        pagina2.set_border_width(10)
        pagina2.add(Gtk.Label(label = "Página 2"))
        carpeta.append_page(pagina2, Gtk.Image.new_from_icon_name("help-about", Gtk.IconSize.MENU))

        self.add(carpeta)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    win = VentanaPrincipal()
    Gtk.main()