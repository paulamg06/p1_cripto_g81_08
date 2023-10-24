"""Fichero que contiene la creación de tokens para las contraseñas"""
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


class Kdf:
    def __init__(self, salt):
        self.scrypt = Scrypt(
            salt=salt,
            length=32,
            n=2**14,
            r=8,
            p=1,
            )
