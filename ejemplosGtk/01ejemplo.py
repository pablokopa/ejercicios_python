import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Definición de la clase VentanaPrincipal que hereda de Gtk.Window
class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        # Configuración del título y tamaño de la ventana
        self.set_title("Ventana Principal")
        self.set_default_size(600, 600)

        # Creación de una caja vertical para contener los widgets
        cajaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # Creación de un stack para gestionar la transición entre widgets
        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)

        # Creación de un botón de check y adición al stack
        chkPulsame = Gtk.CheckButton(label="Púlsame")
        stack.add_titled(chkPulsame, "chk", "Check para pulsar")

        # Creación de una etiqueta y adición al stack
        lblEtiqueta = Gtk.Label()
        lblEtiqueta.set_markup("<big>Etiqueta</big>")
        stack.add_titled(lblEtiqueta, "lbl", "Etiqueta")

        # Creación de un switcher para cambiar entre los elementos del stack
        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)

        # Adición del switcher y el stack a la caja vertical
        cajaV.pack_start(stack_switcher, True, True, 0)
        cajaV.pack_start(stack, True, True, 0)

        # Adición de la caja vertical a la ventana principal
        self.add(cajaV)
        # Conexión del evento de cierre de la ventana con la función Gtk.main_quit
        self.connect("delete-event", Gtk.main_quit)
        # Mostrar todos los widgets
        self.show_all()

# Creación de una instancia de VentanaPrincipal y ejecución del loop principal de GTK
if __name__ == "__main__":
    win = VentanaPrincipal()
    Gtk.main()