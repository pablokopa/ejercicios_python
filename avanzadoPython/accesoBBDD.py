import sqlite3 as dbapi
from sqlite3 import OperationalError, DatabaseError

'''
print(dbapi.apilevel) # Nivel de la API de SQLite
print(dbapi.threadsafety) # Nivel de seguridad de hilos de SQLite
print(dbapi.paramstyle) # Estilo de parámetros utilizado por SQLite
'''

bbdd = dbapi.connect("bbdd.dat")
cursor = bbdd.cursor()

'''
# Crear tabla usuarios en la base de datos
try:
    cursor.execute('create table usuarios (dni text, nombre text, edad int)')
except OperationalError as e:
    print("Error al crear la tabla: ", e)
    bbdd.close()
'''

'''
# Añadir elementos a la base de datos
try:
    cursor.execute('insert into usuarios values ("17384496D","Pablo Iglesias", 21)')
    cursor.execute('insert into usuarios values ("10384592E","Sergio Sanroman", 26)')
    cursor.execute('insert into usuarios values ("82394719C","David Leal", 19)')
    bbdd.commit()
except DatabaseError as e:
    print("Error al insertar datos en la tabla usuarios: ", e)
    bbdd.close()
'''

'''
# Acceder a los datos de la BBDD
try:
    cursor.execute('select dni, nombre, edad from usuarios')
except DatabaseError as e:
    print("Error al hacer la consulta de la tabla usuarios: ", e)
    bbdd.close()

for usuario in cursor.fetchall(): #fecthall() para acceder a todos los datos
    print('Nombre:', usuario[1])
    print('Edad:', usuario[2])
    print('DNI:', usuario[0])
'''

try:
    cursor.execute('select nombre, edad, dni from usuarios where dni = ? and edad = ? ' , ('17384496D', 21))
    print(cursor.fetchone()) #fetchone() para acceder a un dato concreto
except DatabaseError as e:
    print("Error al hacer la consulta de la tabla usuarios: ", e)
    bbdd.close()