import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

# Definición de la clase ListBoxConDatos que hereda de Gtk.ListBoxRow
class ListBoxConDatos(Gtk.ListBoxRow):
    def __init__(self, dato):
        super().__init__()
        self.dato = dato
        # Añadir una etiqueta con el dato al ListBoxRow
        self.add(Gtk.Label(label=dato))

# Definición de la clase VentanaPrincipal que hereda de Gtk.Window
class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        # Configuración del título y tamaño de la ventana
        self.set_title("Ventana Listbox")
        self.set_default_size(600, 220)

        # Creación de una caja vertical principal
        cajaPrincipal = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Creación de un ListBox y configuración del modo de selección
        listBox = Gtk.ListBox()
        listBox.set_selection_mode(Gtk.SelectionMode.NONE)
        cajaPrincipal.pack_start(listBox, True, True, 0)

        # Fila 1
        fila = Gtk.ListBoxRow()
        cajaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        fila.add(cajaH)
        cajaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        cajaH.pack_start(cajaV, True, True, 0)

        # Etiquetas para la primera fila
        lblEtiqueta1 = Gtk.Label(label="Fecha y hora automáticas")
        lblEtiqueta2 = Gtk.Label(label="Acceso a interred")
        cajaV.pack_start(lblEtiqueta1, True, True, 0)
        cajaV.pack_start(lblEtiqueta2, True, True, 0)

        # Switch para la primera fila
        int = Gtk.Switch()
        int.props.valign = Gtk.Align.CENTER
        cajaH.pack_start(int, False, True, 0)
        listBox.add(fila)

        # Fila 2
        fila2 = Gtk.ListBoxRow()
        cajaH2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        fila2.add(cajaH2)

        # Etiqueta y CheckButton para la segunda fila
        lblEtiqueta3 = Gtk.Label(label="Permite actualización automática", xalign=0)
        check = Gtk.CheckButton()
        cajaH2.pack_start(lblEtiqueta3, True, True, 0)
        cajaH2.pack_start(check, False, True, 0)
        listBox.add(fila2)

        # Creación de un segundo ListBox
        listBox2 = Gtk.ListBox()
        elementos = "Una frase larga para dividir".split()

        # Añadir elementos al segundo ListBox
        for palabra in elementos:
            listBox2.add(ListBoxConDatos(palabra))

        # Configuración de la función de ordenación y filtrado
        listBox2.set_sort_func(self.funcion_ordenacion)
        listBox2.set_filter_func(self.funcion_filtrado)
        listBox2.connect("row-activated", self.on_row_activated)
        cajaPrincipal.pack_start(listBox2, True, True, 0)

        # Añadir la caja principal a la ventana
        self.add(cajaPrincipal)
        # Conexión del evento de cierre de la ventana con la función Gtk.main_quit
        self.connect("delete-event", Gtk.main_quit)
        # Mostrar todos los widgets
        self.show_all()

    # Metodo para manejar la activación de una fila
    def on_row_activated(listbox_widget, fila):
        print(fila.dato)

    # Metodo para la función de ordenación
    def funcion_ordenacion(self, fila1, fila2):
        return fila1.dato.lower() > fila2.dato.lower()

    # Metodo para la función de filtrado
    def funcion_filtrado(self, fila):
        return False if fila.dato == "larga" else True

# Creación de una instancia de VentanaPrincipal y ejecución del loop principal de GTK
if __name__ == "__main__":
    win = VentanaPrincipal()
    Gtk.main()