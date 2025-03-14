import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

# Definición de la clase VentanaPrincipal que hereda de Gtk.Window
class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        # Configuración del título y tamaño de la ventana
        self.set_title("Ventana Flowbox")
        self.set_default_size(600, 220)

        # Creación de una ventana con scroll
        scroll = Gtk.ScrolledWindow()
        scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

        # Creación de un FlowBox para contener los botones de colores
        flowbox = Gtk.FlowBox()
        flowbox.set_valign(Gtk.Align.START)
        flowbox.set_max_children_per_line(30)
        flowbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.crea_flowbox(flowbox)
        scroll.add(flowbox)

        # Adición del FlowBox con scroll a la ventana principal
        self.add(scroll)
        # Conexión del evento de cierre de la ventana con la función Gtk.main_quit
        self.connect("delete-event", Gtk.main_quit)
        # Mostrar todos los widgets
        self.show_all()

    # Metodo para crear y añadir botones de colores al FlowBox
    def crea_flowbox(self, flowbox):
        colores = [
            "AliceBlue",
            "AntiqueWhite",
            "AntiqueWhite1",
            "AntiqueWhite2",
            "AntiqueWhite3",
            "AntiqueWhite4",
            "aqua",
            "aquamarine",
            "aquamarine1",
            "aquamarine2",
            "aquamarine3",
            "aquamarine4",
            "azure",
            "azure1",
            "azure2",
            "azure3",
            "azure4",
            "beige",
            "bisque",
            "bisque1",
            "bisque2",
            "bisque3",
            "bisque4",
            "black",
            "BlanchedAlmond",
            "blue",
            "blue1",
            "blue2",
            "blue3",
            "blue4",
            "BlueViolet",
            "brown",
            "brown1",
            "brown2",
            "brown3",
            "brown4",
            "burlywood",
            "burlywood1",
            "burlywood2",
            "burlywood3",
            "burlywood4",
            "CadetBlue",
            "CadetBlue1",
            "CadetBlue2",
            "CadetBlue3",
            "CadetBlue4",
            "chartreuse",
            "chartreuse1",
            "chartreuse2",
            "chartreuse3",
            "chartreuse4",
            "chocolate",
            "chocolate1",
            "chocolate2",
            "chocolate3",
            "chocolate4",
            "coral",
            "coral1",
            "coral2",
            "coral3",
            "coral4"]
        for color in colores:
            boton = self.crear_boton_color(color)
            flowbox.add(boton)

    # Metodo para crear un botón con un área de dibujo del color especificado
    def crear_boton_color(self, color):
        rgba = Gdk.RGBA()
        rgba.parse(color)

        boton = Gtk.Button()

        area = Gtk.DrawingArea()
        area.set_size_request(24, 24)
        area.connect("draw", self.on_draw, {"color":rgba})

        boton.add(area)
        return boton

    # Metodo para dibujar el color en el área de dibujo del botón
    def on_draw(self, control, cr, dic):
        contexto = control.get_style_context()

        ancho = control.get_allocated_width()
        alto = control.get_allocated_height()
        Gtk.render_background(contexto, cr, 0, 0, ancho, alto)

        r, g, b, a = dic["color"]
        cr.set_source_rgba(r, g, b, a)
        cr.rectangle(0, 0, ancho, alto)
        cr.fill()

# Creación de una instancia de VentanaPrincipal y ejecución del loop principal de GTK
if __name__ == "__main__":
    win = VentanaPrincipal()
    Gtk.main()