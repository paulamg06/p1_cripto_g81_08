"""Fichero que gestiona los eventos, calculando la cuenta atrás"""
import sqlite3 as sql
from tkinter import messagebox

class GestionEventos:
    """Clase que se encarga de añadir nuevos eventos a la BBDD y de hacer la cuenta atrás"""
    def __init__(self, db_file):
        self.connection = sql.connect(db_file)
        self.cursor = self.connection.cursor()

        #Creamos una tabla que almacena los eventos
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS eventos 
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL,
                nombre TEXT NOT NULL,
                fecha DATE NOT NULL,
                cuenta_atras TEXT NOT NULL )
        ''')
        self.connection.commit() #Guardamos los cambios

    def crear_evento(self, evento, usuario):
        """Método que añade nuevos eventos al usuario"""
        #Insertamos en la tabla
        self.cursor.execute("INSERT INTO eventos (usuario, nombre, fecha, cuenta_atras) VALUES (?, ?, ?, ?)",
                            (usuario, evento.nombre, evento.fecha, evento.cuenta_atras))
        self.connection.commit() #Guardamos los cambios
        messagebox.showinfo("Éxito", "Nuevo evento creado con éxito")

    def obtener_eventos(self, usuario):
        """Método que obtiene todos los eventos del usuario"""
        self.cursor.execute("SELECT * FROM eventos WHERE usuario=?", (usuario,))
        eventos = self.cursor.fetchall()
        print(eventos)
        return eventos

    def cerrar_conexion(self):
        self.connection.close()
