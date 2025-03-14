import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class ListBoxConDatos(Gtk.ListBoxRow):
    def __init__(self, dato):
        super().__init__()
        self.dato = dato
        self.add(Gtk.Label(label=dato))

class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ventana Listbox")
        self.set_default_size(600, 220)

        cajaPrincipal = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        listBox = Gtk.ListBox()
        listBox.set_selection_mode(Gtk.SelectionMode.NONE)
        cajaPrincipal.pack_start(listBox, True, True, 0)

        # Fila 1
        fila = Gtk.ListBoxRow()
        cajaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        fila.add(cajaH)
        cajaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        cajaH.pack_start(cajaV, True, True, 0)

        lblEtiqueta1 = Gtk.Label(label="Fecha y hora automáticas")
        lblEtiqueta2 = Gtk.Label(label="Acceso a interred")
        cajaV.pack_start(lblEtiqueta1, True, True, 0)
        cajaV.pack_start(lblEtiqueta2, True, True, 0)

        int = Gtk.Switch()
        int.props.valign = Gtk.Align.CENTER
        cajaH.pack_start(int, False, True, 0)
        listBox.add(fila)

        # Fila 2
        fila2 = Gtk.ListBoxRow()
        cajaH2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        fila2.add(cajaH2)

        lblEtiqueta3 = Gtk.Label(label="Permite actualización automática", xalign=0)
        check = Gtk.CheckButton()

        cajaH2.pack_start(lblEtiqueta3, True, True, 0)
        cajaH2.pack_start(check, False, True, 0)
        listBox.add(fila2)

        listBox2 = Gtk.ListBox()
        elementos = "Una frase larga para dividir".split()

        for palabra in elementos:
            listBox2.add(ListBoxConDatos(palabra))

        listBox2.set_sort_func(self.funcion_ordenacion)
        listBox2.set_filter_func(self.funcion_filtrado)
        listBox2.connect("row-activated", self.on_row_activated)
        cajaPrincipal.pack_start(listBox2, True, True, 0)

        self.add(cajaPrincipal)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_row_activated(listbox_widget, fila):
        print(fila.dato)

    def funcion_ordenacion(self, fila1, fila2):
        return fila1.dato.lower() > fila2.dato.lower()

    def funcion_filtrado(self, fila):
        return False if fila.dato == "larga" else True

if __name__ == "__main__":
    win = VentanaPrincipal()
    Gtk.main()