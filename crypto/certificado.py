"""Fichero que contiene la clase para crear el cifrado digital"""
from cryptography.hazmat.primitives.asymetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key

class Certificado():
    """Clase que se encarga de realizar el certificado digital"""
    def __init__(self, file: None):
        if not file:
            # Genera la clave privada
            self.private_key = rsa.generate_private_key(
                public_exponent = 65537,
                key_size=2048
            )
        else:
            self.private_key = self.key_loading(file)
        self.public_key = self.private_key.public_key()

    def public_serialization(self):
        """Método que serializa la clave pública"""
        pem = self.public_key.public_bytes(
            encoding = serialization.Encoding.PEM,
            format = serialization.PublicFormat.SubjectPublicKeyInfo
        )
        pem.splitlines()[0]
        b'-----BEGIN PUBLIC KEY-----'

    def private_serialization(self):
        """Método que serializa la clave privada"""
        pem = self.private_key.private_bytes(
            encoding = serialization.Encoding.PEM,
            format = serialization.PrivateFormat.PKCS8,
            encryption_algorithm = serialization.BestAvailableEncryption(b'mypassword')
        )
        pem.splitlines()[0]
        b'-----BEGIN ENCRYPTED PRIVATE KEY-----'

    def key_loading(self, file):
        """Método que carga una clave privada"""
        with open(file, "rb") as key_file:
            return serialization.load_pem_private_key(
                key_file.read(),
                password = None
            )
