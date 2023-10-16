"""Fichero que gestiona los eventos, calculando la cuenta atrás"""
import base64
import os
import sqlite3 as sql
from tkinter import messagebox
from crypto.tokens import Tokens
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305


class GestionEventos:
    """Clase que se encarga de añadir nuevos eventos a la BBDD y de hacer la cuenta atrás"""

    def __init__(self, db_file):
        self.connection = sql.connect(db_file)
        self.cursor = self.connection.cursor()

        """self.cursor.execute('''
                        DROP TABLE eventos 
                        ''')"""
        # Creamos una tabla que almacena los eventos
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS eventos 
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL,
                nombre_cifrado TEXT NOT NULL,
                nonce_nombre TEXT NOT NULL,
                fecha_cifrada TEXT NOT NULL,
                nonce_fecha TEXT NOT NULL,
                cuenta_atras_cifrada TEXT NOT NULL,
                nonce_c_a TEXT NOT NULL)
        ''')
        self.connection.commit()  # Guardamos los cambios

    def crear_evento(self, evento, usuario, data_key):
        """Método que añade nuevos eventos al usuario"""

        # Generar los nonce
        chacha = ChaCha20Poly1305(data_key)
        nonce1 = os.urandom(12)
        nonce2 = os.urandom(12)
        nonce3 = os.urandom(12)

        # Pasar datos a bytes
        nombre_bytes = bytes(evento.nombre, 'ascii')
        fecha_bytes = bytes(str(evento.fecha), 'ascii')
        cuenta_atras_bytes = bytes(evento.cuenta_atras, 'utf-8')

        # Cifrar los datos
        nombre_cif = chacha.encrypt(nonce1, nombre_bytes, None)
        fecha_cif = chacha.encrypt(nonce2, fecha_bytes, None)
        cuenta_atras_cif = chacha.encrypt(nonce3, cuenta_atras_bytes, None)

        # Pasar a ascii los nonce para guardarlos
        nonce1_b64 = base64.b64encode(nonce1)
        nonce1_ascii = nonce1_b64.decode()

        nonce2_b64 = base64.b64encode(nonce2)
        nonce2_ascii = nonce2_b64.decode()

        nonce3_b64 = base64.b64encode(nonce3)
        nonce3_ascii = nonce3_b64.decode()

        self.cursor.execute('''INSERT INTO eventos (usuario, nombre_cifrado, nonce_nombre, fecha_cifrada, 
        nonce_fecha, cuenta_atras_cifrada, nonce_c_a) VALUES (?, ?, ?, ?, ?, ?, ?)''',
                            (usuario, nombre_cif, nonce1_ascii, fecha_cif,
                             nonce2_ascii, cuenta_atras_cif, nonce3_ascii))
        self.connection.commit()  # Guardamos los cambios
        messagebox.showinfo("Éxito", "Nuevo evento creado con éxito")

    def obtener_eventos(self, usuario, data_key):
        """Método que obtiene todos los eventos del usuario"""
        chacha = ChaCha20Poly1305(data_key)

        self.cursor.execute("SELECT * FROM eventos WHERE usuario=?", (usuario,))
        eventos_cifrados = self.cursor.fetchall()
        eventos = []

        for tupla in eventos_cifrados:
            nueva_tupla = self.descifrar_evento(chacha, tupla)
            eventos.append(nueva_tupla)

        return eventos

    def borrar_evento(self, evento, usuario, data_key):
        """Método que borra los eventos del usuario"""
        chacha = ChaCha20Poly1305(data_key)

        self.cursor.execute("SELECT * FROM eventos WHERE usuario=?", (usuario,))
        eventos_cifrados = self.cursor.fetchall()
        for tupla in eventos_cifrados:
            evento_descifrado = self.descifrar_evento(chacha, tupla)
            if (evento_descifrado[0] == evento[0]) and (evento_descifrado[1] == evento[1]):
                self.cursor.execute("DELETE FROM eventos WHERE usuario=? AND nombre_cifrado=? AND fecha_cifrada=?",
                                    (usuario, tupla[2], tupla[4]))
        self.connection.commit()  # Guardamos los cambios
        messagebox.showinfo("Éxito", "Evento eliminado con éxito")

    def descifrar_evento(self, chacha, tupla):

        nombre_cif = tupla[2]
        fecha_cif = tupla[4]
        cuenta_atras_cif = tupla[6]

        nonce1_ascii = tupla[3]
        nonce2_ascii = tupla[5]
        nonce3_ascii = tupla[7]

        # Pasar los nonce de ascii a bytes
        nonce1_b64 = bytes(nonce1_ascii, 'ascii')
        nonce1 = base64.b64decode(nonce1_b64)
        nonce2_b64 = bytes(nonce2_ascii, 'ascii')
        nonce2 = base64.b64decode(nonce2_b64)
        nonce3_b64 = bytes(nonce3_ascii, 'ascii')
        nonce3 = base64.b64decode(nonce3_b64)

        nombre_bytes = chacha.decrypt(nonce1, nombre_cif, None)
        fecha_bytes = chacha.decrypt(nonce2, fecha_cif, None)
        cuenta_atras_bytes = chacha.decrypt(nonce3, cuenta_atras_cif, None)

        #Pasar a ascii los datos del evento para leerlos
        nombre = nombre_bytes.decode()
        fecha = fecha_bytes.decode()
        cuenta_atras = cuenta_atras_bytes.decode()

        return nombre, fecha, cuenta_atras

    def cerrar_conexion(self):
        self.connection.close()
