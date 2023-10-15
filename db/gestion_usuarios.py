"""Fichero que contiene el registro de los usuarios"""
import sqlite3 as sql
from tkinter import messagebox
from crypto.tokens import Tokens

class GestionUsuarios:
    """Clase que contiene el registro de los usuarios"""
    def __init__(self, db_file):
        self.connection = sql.connect(db_file)
        self.cursor = self.connection.cursor()
        self.usuarios = [] #Lista que almacena los usuarios que se registran

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios 
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL,
        token TEXT NOT NULL)
        ''')

        self.connection.commit()

    def agregar_usuario(self, usuario, contrasena):
        """Método que regitra a los usuarios añadiéndolos a la lista de usuarios"""
        try:
            #primero derivamos la contraseña
            token = Tokens(contrasena)
            self.cursor.execute("INSERT INTO usuarios (usuario,token) VALUES (?,?)", (usuario,token.key))
            self.connection.commit()
            return True
        except sql.Error as exception:
            messagebox.showerror("Error", "Error al agregar usuario:" + str(exception))
            return False

    def verificar_credenciales(self, usuario, contrasena):
        """Método que verifica el inicio de sesión del usuario"""
        #derivamos la contraseña
        token = Tokens(contrasena)
        #verificamos el token
        self.cursor.execute("SELECT * FROM usuarios WHERE usuario=? AND token=?", (usuario,token.key))
        resultado = self.cursor.fetchone()
        return resultado is not None

    def borrar_usuario(self, usuario):
        """Método para borrar un usuario de la base de datos"""
        # Verificamos que el usuario no exista
        try:
            self.cursor.execute("DELETE FROM usuarios WHERE usuario=?", [usuario])
            self.connection.commit()
            messagebox.showerror("Éxito", "Usuario eliminado con éxito")
            return True
        except sql.Error as exception:
            messagebox.showerror("Error", "Error al eliminar el usuario:" + str(exception))
            return False

    def cerrar_conexion(self):
        self.connection.close()
