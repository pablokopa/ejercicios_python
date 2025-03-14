import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib


# Definición de la clase Aplicacion
class Aplicacion:
    def __init__(self):
        # Creación del constructor de la interfaz desde el archivo Glade
        builder = Gtk.Builder()
        builder.add_from_file("01checksGlade.glade")

        # Obtención de la ventana principal y el campo de texto
        ventana = builder.get_object("ventanaPrincipal")
        self.txtTexto = builder.get_object("txtTexto")

        # Conexión de las señales definidas en Glade con los métodos correspondientes
        builder.connect_signals({
            "on_VentanaPrincipal_destroy": self.on_ventanaPrincipal_destroy,
            "on_chkEditable_toggled": self.on_chkEditable_toggled,
            "on_chkVisible_toggled": self.on_chkVisible_toggled,
            "on_chkIcona_toggled": self.on_chkIcona_toggled,
            "on_chkPulso_toggled": self.on_chkPulso_toggled
        })

        # Mostrar todos los widgets de la ventana
        ventana.show_all()

    # Metodo para manejar el evento de cierre de la ventana principal
    def on_ventanaPrincipal_destroy(self, widget):
        Gtk.main_quit()

    # Metodo para manejar el evento de cambio del estado del checkbox "Editable"
    def on_chkEditable_toggled(self, boton):
        pulsado = boton.get_active()
        self.txtTexto.set_editable(pulsado)

    # Metodo para manejar el evento de cambio del estado del checkbox "Visible"
    def on_chkVisible_toggled(self, boton):
        self.txtTexto.set_visible(boton.get_active())

    # Metodo para manejar el evento de cambio del estado del checkbox "Icona"
    def on_chkIcona_toggled(self, boton):
        if boton.get_active():
            nome_icona = "system-search-symbolic"
        else:
            nome_icona = None
        self.txtTexto.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, nome_icona)

    # Metodo para manejar el evento de cambio del estado del checkbox "Pulso"
    def on_chkPulso_toggled(self, boton):
        if boton.get_active():
            self.txtTexto.set_progress_pulse_step(0.2)
            self.temporizacion = GLib.timeout_add(100, self.do_pulso, None)

    # Metodo para realizar el pulso en el campo de texto
    def do_pulso(self):
        self.txtTexto.progress_pulse()
        return True


# Creación de una instancia de Aplicacion y ejecución del loop principal de GTK
if __name__ == "__main__":
    app = Aplicacion()
    Gtk.main()