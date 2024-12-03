import sqlite3 as dbapi

class ConexionBD:
    def __init__(self, rutaBd):
        self.rutaBd = rutaBd
        self.conexion = None
        self.cursor = None

    # Conectarse a la base de datos
    def conectaBD(self):
        try:
            if self.conexion is None:
                if self.rutaBd is None:
                    print("La ruta de la base de datos es: None ")
                else:
                    self.conexion = dbapi.connect(self.rutaBd)
            else:
                print("Base de datos conectada: " + self.conexion)

        except dbapi.StandardError as e:
            print("Error al hacer la conexión a la base de datos " + self.rutaBd + ": " + e)
        else:
            print("Conexión de base de datos realizada")

    # Crear cursor
    def creaCursor(self):
        try:
            if self.conexion is None:
                print("Creando el cursor: Es necesario realizar la conexión a la base de datos previamente")


            else:
                if self.cursor is None:
                    self.cursor = self.conexion.cursor()
                else:
                    print("El cursor ya está inicializado: " + self.cursor)


        except dbapi.Error as e:
            print(e)
        else:
            print("Cursor preparado")

    # Hacer una consulta sin parametros
    def consultaSenParametros(self, consultaSQL):
        listaConsulta = list()
        try:
            if self.conexion is None:
                print("Creando consulta: Es necesario realizar la conexión a la base de datos previamente")
            else:
                if self.cursor is None:
                    print("Creando consulta: Es necesario realizar la creación del cursor previamente")
                else:
                    self.cursor.execute(consultaSQL)

                    for fila in self.cursor.fetchall():
                        listaConsulta.append(fila)

        except dbapi.DatabaseError as e:
            print("Error haciendo la consulta: " + str(e))
            return None
        else:
            print("Consulta ejecutada")
            return listaConsulta

    # Hacer una consulta con parametros (?)
    def consultaConParametros(self, consultaSQL, *parametros):
        listaConsulta = list()
        try:
            if self.conexion is None:
                print("Creando consulta: Es necesario realizar la conexión a la base de datos previamente")
            else:
                if self.cursor is None:
                    print("Creando consulta: Es necesario realizar la creación del cursor previamente")
                else:
                    self.cursor.execute(consultaSQL, parametros)

                    for fila in self.cursor.fetchall():
                        listaConsulta.append(fila)

        except dbapi.DatabaseError as e:
            print("Error haciendo la consulta: " + str(e))
            return None
        else:
            print("Consulta ejecutada")
            return listaConsulta

    # Cerrar conexión a la base de datos
    def pechaBD(self):
        self.cursor.close()
        self.conexion.close()