"""Fichero que contiene la creación de tokens para las contraseñas"""
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


class Tokens:
    def __init__(self, password, salt):
        self.password = password
        self.kdf = Scrypt(
            salt=salt,
            length=32,
            n=2**14,
            r=8,
            p=1,
            )

    #derivamos la clave
    def derivar(self):
        return self.kdf.derive(bytes(self.password, 'utf-8'))

    def verificar(self, key):
        """Método para verificar que la contraseña introducida sea la misma"""
        self.kdf.verify(bytes(self.password, 'utf-8'), key)
