"""Fichero que contiene el registro de los usuarios"""

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
        self.usuarios.append((usuario, contrasena))
        return True

    def verificar_credenciales(self, usuario, contrasena):
        """Método que verifica el inicio de sesión del usuario"""
        for user, contra in self.usuarios:
            #Si coinciden, los parámetros son correctos
            if user == usuario and contra == contrasena:
                return True

        #Si no ha encontrado coincidencias, es porque los parámetros no son correctos
        return False
