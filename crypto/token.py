"""Fichero que contiene la clase para codificar y decodificar las contraseñas de los usuarios"""
import os
import base64
from crypto.kdf import Kdf

class Token:
    """Clase que contiene el método para crear los tokens"""
    def __init__(self, contrasena, salt):
        self.contrasena = contrasena
        self.salt_deriv_key = os.urandom(16)
        self.salt = salt
        self.key_ascii, self.salt_ascii, self.salt_deriv_key_ascii = self.codificar()

    def codificar(self):
        """Método que crea los tokens y codifica"""
        # creamos el kdf
        kdf = Kdf(self.salt)

        # derivamos la clave
        key = kdf.scrypt.derive(bytes(self.contrasena, 'utf-8'))

        # pasamos a ascii para guardarlos
        key_b64 = base64.b64encode(key)
        key_ascii = key_b64.decode()

        salt_b64 = base64.b64encode(self.salt)
        salt_ascii = salt_b64.decode()

        salt_deriv_key_b64 = base64.b64encode(self.salt_deriv_key)
        salt_deriv_key_ascii = salt_deriv_key_b64.decode()

        return key_ascii, salt_ascii, salt_deriv_key_ascii
