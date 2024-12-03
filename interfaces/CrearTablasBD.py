import sys
from conexionBD import ConexionBD

class CrearTablasBD:
    def __init__(self):
        super().__init__()
        self.bDatos = ConexionBD("usuarios.bd")
        self.bDatos.conectaBD()
        self.bDatos.creaCursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.bDatos.cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nombre TEXT, dni TEXT, genero TEXT, fallecido INTEGER)")
        self.bDatos.conexion.commit()

    def insertar_usuario(self, nombre, dni, genero, fallecido):
        self.bDatos.cursor.execute("INSERT INTO usuarios (nombre, dni, genero, fallecido) VALUES (?, ?, ?, ?)",
                                   (nombre, dni, genero, fallecido))
        self.bDatos.conexion.commit()

    def eliminar_usuario(self, dni):
        self.bDatos.cursor.execute("DELETE FROM usuarios WHERE dni = ?", (dni,))
        self.bDatos.conexion.commit()

    def actualizar_usuario(self, nombre, dni, genero, fallecido):
        self.bDatos.cursor.execute("UPDATE usuarios SET nombre = ?, genero = ?, fallecido = ? WHERE dni = ?",
                                   (nombre, genero, fallecido, dni))
        self.bDatos.conexion.commit()

    def consultar_usuarios(self):
        self.bDatos.cursor.execute("SELECT * FROM usuarios")
        return self.bDatos.cursor.fetchall()

    def cerrar_conexion(self):
        self.bDatos.pechaBD()

if __name__ == '__main__':
    creaTablas = CrearTablasBD()