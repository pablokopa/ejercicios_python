import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class VentanaPrincipal(Gtk.Window):
    def __init__(self):
# Inicializar la clase padre
        super().__init__()
        self.set_title("Ejemplo Gtk ComboBox")

# Crear un modelo de datos
        modelo = Gtk.ListStore(int, str)
        modelo.append((1, "Ana Pérez"))
        modelo.append((2, "Juan López"))
        modelo.append((3, "María Gómez"))
        modelo.append((4, "Pedro Martínez"))
        modelo.append((5, "Luisa Sánchez"))
        modelo.append((6, "Sara García"))
        modelo.append((7, "Carlos Fernández"))
        modelo.append((8, "Sonia Rodríguez"))

# Crear un layout de caja vertical
        cajaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

# Crear un nuevo ComboBox a partir del modelo
        cmbNomes = Gtk.ComboBox.new_with_model_and_entry(modelo)
        cmbNomes.set_entry_text_column(1) # Columna de texto
        cmbNomes.connect("changed", self.on_cmbNomes_changed)
        txtCuadroTexto = cmbNomes.get_child() # Obtener el cuadro de texto
        txtCuadroTexto.connect("activate", self.on_txtCuadroTexto_activate, modelo)
        cajaV.pack_start(cmbNomes, False, False, 0) # Añadir al layout

# Crear un ComboBox con un modelo de datos de paises
        modelo_paises = Gtk.ListStore(str)
        paises = ["España", "Francia", "Italia", "Portugal", "Alemania",
                  "Reino Unido", "Irlanda", "Bélgica", "Holanda", "Suiza"]
        for pais in paises:
            modelo_paises.append((pais,))
        cmbPaises = Gtk.ComboBox.new_with_model(modelo_paises)
        celdaTexto = Gtk.CellRendererText()
        cmbPaises.pack_start(celdaTexto, True)
        cmbPaises.add_attribute(celdaTexto, "text", 0)
        cajaV.pack_start(cmbPaises, False, False, 0)

# Añadir la caja al contenedor principal y mostrar la ventana
        self.add(cajaV)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

# Metodo que escribe en la consola el nombre seleccionado en el ComboBox
    def on_cmbNomes_changed(self, combo):
        fila = combo.get_active_iter()
        if fila is not None:
            modelo = combo.get_model()
            num, nome = modelo [fila][:2]
            print("Nombre: %s - Número: %d" % (nome, num))

# Metodo que escribe el texto introducido y añade una nueva fila al ComboBox
    def on_txtCuadroTexto_activate(self, cuadroTexto, mod):
        print("Teclado: %s" % cuadroTexto.get_text())
        mod.append((9, cuadroTexto.get_text()))

if __name__ == "__main__":
    try:
        win = VentanaPrincipal()
        Gtk.main()
    except KeyboardInterrupt:
        print("Programa interrumpido por el usuario")