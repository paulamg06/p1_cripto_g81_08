"""Fichero que gestiona los eventos, calculando la cuenta atrás"""
import sqlite3 as sql
from tkinter import messagebox
from crypto.cifrado import Cifrado, Descifrado


class GestionEventos:
    """Clase que se encarga de añadir nuevos eventos a la BBDD y de hacer la cuenta atrás"""

    def __init__(self, db_file):
        self.connection = sql.connect(db_file)
        self.cursor = self.connection.cursor()

        """self.cursor.execute('''
                        DROP TABLE eventos 
                        ''')"""
        # creamos una tabla que almacena los eventos
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS eventos 
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL,
                nombre_cifrado BLOB NOT NULL,
                nonce_nombre TEXT NOT NULL,
                fecha_cifrada BLOB NOT NULL,
                nonce_fecha TEXT NOT NULL,
                cuenta_atras_cifrada BLOB NOT NULL,
                nonce_c_a TEXT NOT NULL)
        ''')
        self.connection.commit()  # guardamos los cambios

    def crear_evento(self, evento, usuario, data_key):
        """Método que añade nuevos eventos al usuario"""
        # generamos una clase para cada dato
        nombre = Cifrado(evento.nombre, data_key)
        fecha = Cifrado(evento.fecha, data_key)
        cuenta_atras = Cifrado(evento.cuenta_atras, data_key)

        # insertamos los datos descifrados con sus respectivos nonce en la tabla
        self.cursor.execute('''INSERT INTO eventos (usuario, nombre_cifrado, nonce_nombre, fecha_cifrada, 
        nonce_fecha, cuenta_atras_cifrada, nonce_c_a) VALUES (?, ?, ?, ?, ?, ?, ?)''',
                            (usuario, nombre.dato_cifrado, nombre.nonce_ascii, fecha.dato_cifrado,
                             fecha.nonce_ascii, cuenta_atras.dato_cifrado, cuenta_atras.nonce_ascii))
        self.connection.commit()  # guardamos los cambios
        messagebox.showinfo("Éxito", "Nuevo evento creado con éxito")

    def obtener_eventos(self, usuario, data_key):
        """Método que obtiene todos los eventos del usuario"""
        # obtenemos los eventos del usuario
        self.cursor.execute("SELECT * FROM eventos WHERE usuario=?", (usuario,))

        eventos_cifrados = self.cursor.fetchall()
        eventos = []

        # pasamos por cada evento para ir descifrándolos
        for row in eventos_cifrados:
            # generamos una clase de descifrado para cada dato
            nombre = Descifrado(row[2], row[3], data_key)
            fecha = Descifrado(row[4], row[5], data_key)
            cuentra_atras = Descifrado(row[6], row[7], data_key)

            # incluimos cada dato en una tupla para añadirlos a la lista de eventos
            tupla_aux = (nombre.dato, fecha.dato, cuentra_atras.dato)
            eventos.append(tupla_aux)

        return eventos

    def borrar_evento(self, evento, usuario, data_key):
        """Método que borra los eventos del usuario"""
        # obtenemos todos los eventos del usuario
        self.cursor.execute("SELECT * FROM eventos WHERE usuario=?", (usuario,))
        eventos_cifrados = self.cursor.fetchall()

        # pasamos por cada evento para ver cuál coincide con el que el usuario quiere borrar
        for row in eventos_cifrados:
            nombre = Descifrado(row[2], row[3], data_key)
            fecha = Descifrado(row[4], row[5], data_key)

            if (nombre.dato == evento[0]) and (fecha.dato == evento[1]):
                self.cursor.execute("DELETE FROM eventos WHERE usuario=? AND nombre_cifrado=? AND fecha_cifrada=?",
                                    (usuario, row[2], row[4]))

        self.connection.commit()  # guardamos los cambios
        messagebox.showinfo("Éxito", "Evento eliminado con éxito")

    def cerrar_conexion(self):
        self.connection.close()
