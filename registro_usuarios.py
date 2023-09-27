"""Fichero que contiene el registro de los usuarios"""
import sqlite3 as sql
from tkinter import messagebox

class RegistroUsuarios:
    """Clase que contiene el registro de los usuarios"""
    def __init__(self, db_file):
        self.connection = sql.connect(db_file)
        self.cursor = self.connection.cursor()
        self.usuarios = [] #Lista que almacena los usuarios que se registran

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios 
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL,
        contrasena TEXT NOT NULL)
        ''')

        self.connection.commit()

    def agregar_usuario(self, usuario, contrasena):
        """Método que regitra a los usuarios añadiéndolos a la lista de usuarios"""
        #Verificamos que el usuario no exista
        try:
            self.cursor.execute("INSERT INTO usuarios (usuario,contrasena) VALUES (?,?)", (usuario,contrasena))
            self.connection.commit()
            return True
        except sql.Error as exception:
            messagebox.showerror("Error", "Error al agregar usuario:" + str(exception))
            return False

    def verificar_credenciales(self, usuario, contrasena):
        """Método que verifica el inicio de sesión del usuario"""
        self.cursor.execute("SELECT * FROM usuarios WHERE usuario=? AND contrasena=?", (usuario,contrasena))
        resultado = self.cursor.fetchone()
        return resultado is not None

    def cerrar_conexion(self):
        self.connection.close()
