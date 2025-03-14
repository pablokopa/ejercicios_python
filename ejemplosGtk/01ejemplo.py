import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ventana Principal")
        self.set_default_size(600, 600)

        cajaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)

        chkPulsame = Gtk.CheckButton(label="Púlsame")
        stack.add_titled(chkPulsame, "chk", "Check para pulsar")

        lblEtiqueta = Gtk.Label()
        lblEtiqueta.set_markup("<big>Etiqueta</big>")
        stack.add_titled(lblEtiqueta, "lbl", "Etiqueta")

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)

        cajaV.pack_start(stack_switcher, True, True, 0)
        cajaV.pack_start(stack, True, True, 0)

        self.add(cajaV)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    win = VentanaPrincipal()
    Gtk.main()