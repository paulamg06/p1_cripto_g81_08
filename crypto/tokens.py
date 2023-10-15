"""Fichero que contiene la creación de tokens para las contraseñas"""

import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

salt = os.urandom(16)

class Tokens:
    def __init__(self, password):
        self.kdf = Scrypt(
            salt=salt,
            length=32,
            n=2**14,
            r=8,
            p=1,
            )

        #derivamos la clave
        self.key = self.kdf.derive(bytes(password, 'utf-8'))


    def verificar(self, password):
        """Método para verificar que la contraseña introducida sea la misma"""
        self.kdf.verify(password, self.key)
