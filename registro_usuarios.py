"""Fichero que contiene el registro de los usuarios"""
import sqlite3 as sql

class RegistroUsuarios:
    """Clase que contiene el registro de los usuarios"""
    def __init__(self):
        self.usuarios = [] #Lista que almacena los usuarios que se registran

    def agregar_usuario(self, usuario, contrasena):
        """Método que regitra a los usuarios añadiéndolos a la lista de usuarios"""
        #Verificamos que el usuario no exista
        for user, contra in self.usuarios:
            #Si el usuario ya existe, no se crea nada
            if user == usuario:
                return False

        #Añadimos el nuevo usuario a nuestra lista
        self.registrar_base_datos(usuario, contrasena)
        return True

    def verificar_credenciales(self, usuario, contrasena):
        """Método que verifica el inicio de sesión del usuario"""
        for user, contra in self.usuarios:
            #Si coinciden, los parámetros son correctos
            if user == usuario and contra == contrasena:
                return True

        #Si no ha encontrado coincidencias, es porque los parámetros no son correctos
        return False

    def registrar_base_datos(self, usuario, contrasena):
        """Método para registrar el usuario en la base de datos"""
        #Conexion
        conection = sql.connect("sqllite")
        #Cursor
        cursor = conection.cursor()

        #Insertamos los datos
        consulta = "INSERT INTO usuarios (nombre, contrasena) VALUES (?, ?)"
        datos_usuario = (str(usuario), str(contrasena))

        #Consulta
        cursor.execute(consulta, datos_usuario)

        #Confirmamos
        conection.commit()
