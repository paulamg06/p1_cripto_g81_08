"""Fichero que contiene las funciones para la parte de la firma"""
import os
import string
from random import random
from db.gestion_evento import GestionEventos

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.serialization import load_pem_public_key


def save_priv_key():
    """Función que serializa y guarda la clave privada"""
    # Genera la clave privada
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # Serializa la clave privada y la guarda
    priv_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(bytes(generar_contrasena(), 'ascii'))
    )
    with open("priv_key.pem", "wb") as priv_key_file:
        priv_key_file.write(priv_pem)


def generar_contrasena():
    """Función que genera una contraseña a partir de variables de entorno"""
    # Guarda variable de entorno
    var_entorno = os.getenv("COMPUTERNAME")

    width = 12
    char = string.ascii_letters + string.digits + string.punctuation

    # Genera la contraseña a partir de la variable de entorno
    random.seed(var_entorno)
    return ''.join(random.choice(char) for _ in range(width))


def cargar_priv_key():
    """Función que carga una clave privada a partir de un archivo"""
    with open("priv_key.pem", "rb") as key_file:
        return serialization.load_pem_private_key(
            key_file.read(),
            password=bytes(generar_contrasena(), 'ascii')
        )


def serialization():
    """Función que serializa las claves y las guarda en un .pem"""
    private_key = cargar_priv_key()

    # Genera la clave pública a través de la privada
    public_key = private_key.public_key()

    # Serializa la clave publica y la guarda
    pub_pem = public_key.public_bytes(
        encoding = serialization.Encoding.PEM,
        format = serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open("pub_key.pem", "wb") as pub_key_file:
        pub_key_file.write(pub_pem)


def deserialization():
    """Función que deserializa la clave publica"""
    key = load_pem_public_key(public_pem_data)
    return isinstance(key, rsa.RSAPublicKey)


def firmar(db_file, usuario, data_key):
    """Función que devuelve la firma"""
    # Carga lo que se quiere firmar
    gestion_evento = GestionEventos(db_file)
    message = gestion_evento.obtener_eventos(usuario, data_key)

    # Pasa a bytes la info
    b64_message = bytes(message, "ascii")

    # Carga la clave privada
    private_key = cargar_priv_key()

    # Firma y se guarda
    signature = private_key.sign(
        b64_message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    guardar_firma(signature)


def guardar_firma(signature):
    """Función que guarda la firma"""
    with open("firma.sig", "wb") as signature_file:
        signature_file.write(signature)


def verificar_firma(signature, b64_message):
    """Función que verifica la firma"""
    # Carga la clave privada
    private_key = cargar_priv_key()

    # Carga la clave publica
    public_key = private_key.public_key()

    # Verifica la clave publica
    public_key.verify(
        signature,
        b64_message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
