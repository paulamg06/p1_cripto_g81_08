"""Fichero que contiene la clase para llevar a cabo el cifrado y descifrado de nuestra aplicación"""
import base64
import os
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305

class Cifrado:
    """Clase que contiene el método para el cifrado de datos"""
    def __init__(self, dato, data_key):
        self.chacha = ChaCha20Poly1305(data_key)
        self.dato_cifrado, self.nonce_ascii = self.cifrar(dato)

    def cifrar(self, dato):
        """Método que cifra los datos"""
        nonce = os.urandom(12)

        # pasa los datos a bytes
        if type(dato) is not str:
            dato_bytes = bytes(str(dato), 'ascii')
        else:
            dato_bytes = bytes(dato, 'utf-8')

        # cifrado de datos y del nonce
        dato_cifrado = self.chacha.encrypt(nonce, dato_bytes, None)

        nonce_b64 = base64.b64encode(nonce)
        nonce_ascii = nonce_b64.decode()

        return dato_cifrado, nonce_ascii

class Descifrado:
    """Clase que contiene el método para descifrar los datos"""

    def __init__(self, dato_cifrado, nonce_ascii, data_key):
        self.dato_cifrado = dato_cifrado
        self.chacha = ChaCha20Poly1305(data_key)
        self.dato = self.descifrar(dato_cifrado, nonce_ascii)

    def descifrar(self, dato_cifrado, nonce_ascii):
        """Método que descifra los datos"""
        # pasamos el nonce a bytes
        nonce_b64 = bytes(nonce_ascii, 'ascii')
        nonce = base64.b64decode(nonce_b64)

        # desciframos el dato
        dato_bytes = self.chacha.decrypt(nonce, dato_cifrado, None)

        dato = dato_bytes.decode()

        return dato
