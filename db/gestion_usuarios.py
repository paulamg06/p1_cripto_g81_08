"""Fichero que contiene el registro de los usuarios"""
import base64
import os
import sqlite3 as sql
from tkinter import messagebox
from crypto.tokens import Tokens


class GestionUsuarios:
    """Clase que contiene el registro de los usuarios"""

    def __init__(self, db_file):
        self.connection = sql.connect(db_file)
        self.cursor = self.connection.cursor()
        self.usuarios = []  # Lista que almacena los usuarios que se registran

        """self.cursor.execute('''
                DROP TABLE usuarios 
                ''')"""

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios 
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL,
        token TEXT NOT NULL,
        salt TEXT NOT NULL,
        salt_deriv_key NOT NULL)
        ''')

        self.connection.commit()

    def agregar_usuario(self, usuario, contrasena):
        """Método que regitra a los usuarios añadiéndolos a la lista de usuarios"""
        try:
            # primero derivamos la contraseña
            salt = os.urandom(16)
            salt_deriv_key = os.urandom(16)

            token = Tokens(contrasena, salt)
            key_b64 = base64.b64encode(token.key)
            key_ascii = key_b64.decode()

            salt_b64 = base64.b64encode(salt)
            salt_ascii = salt_b64.decode()

            salt_deriv_key_b64 = base64.b64encode(salt_deriv_key)
            salt_deriv_key_ascii = salt_deriv_key_b64.decode()

            self.cursor.execute("INSERT INTO usuarios (usuario,token,salt,salt_deriv_key) VALUES (?,?,?,?)",
                                (usuario, key_ascii, salt_ascii, salt_deriv_key_ascii))
            self.connection.commit()
            return True
        except sql.Error as exception:
            messagebox.showerror("Error", "Error al agregar usuario:" + str(exception))
            return False

    def verificar_credenciales(self, usuario, contrasena):
        """Método que verifica el inicio de sesión del usuario"""

        # verificamos el token
        self.cursor.execute("SELECT token, salt FROM usuarios WHERE usuario=?", [usuario])
        resultado = self.cursor.fetchone()

        if resultado is None:
            return None

        key_ascii = resultado[0]
        key_b64 = bytes(key_ascii, 'ascii')
        key = base64.b64decode(key_b64)

        salt_ascii = resultado[1]
        salt_b64 = bytes(salt_ascii, 'ascii')
        salt = base64.b64decode(salt_b64)

        token = Tokens(contrasena, salt)
        return token.verificar(key)

    def obtener_data_key(self, usuario, contrasena):
        self.cursor.execute("SELECT salt_deriv_key FROM usuarios WHERE usuario=?", [usuario])
        resultado = self.cursor.fetchone()
        salt_deriv_key_ascii = resultado[0]
        salt_deriv_key_b64 = bytes(salt_deriv_key_ascii, 'ascii')
        salt_deriv_key = base64.b64decode(salt_deriv_key_b64)

        data_key = Tokens(contrasena, salt_deriv_key).key
        return data_key

    def borrar_usuario(self, usuario):
        """Método para borrar un usuario de la base de datos"""
        # Verificamos que el usuario no exista
        try:
            self.cursor.execute("DELETE FROM usuarios WHERE usuario=?", [usuario])
            self.cursor.execute("SELECT * FROM eventos WHERE usuario=?", (usuario,))
            eventos = self.cursor.fetchall()
            for ii in range(len(eventos)):
                self.cursor.execute("DELETE FROM eventos WHERE usuario=?", [usuario])
            self.connection.commit()
            messagebox.showerror("Éxito", "Usuario eliminado con éxito")
            return True
        except sql.Error as exception:
            messagebox.showerror("Error", "Error al eliminar el usuario:" + str(exception))
            return False

    def cerrar_conexion(self):
        self.connection.close()
