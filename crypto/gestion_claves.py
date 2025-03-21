"""Fichero que contiene las funciones relacionadas con la gestion de las claves"""
import os
import string
import random

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key


def generar_contrasena():
    """Función que genera una contraseña a partir de variables de entorno"""
    # Guarda variable de entorno
    var_entorno = os.getenv("MI_VAR")

    width = 12
    char = string.ascii_letters + string.digits + string.punctuation

    # Genera la contraseña a partir de la variable de entorno
    random.seed(var_entorno)
    return ''.join(random.choice(char) for _ in range(width))


def save_priv_key():
    """Función que serializa y guarda la clave privada"""
    # Genera la clave privada
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # Serializa la clave privada y la guarda
    try:
        priv_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(bytes(generar_contrasena(), 'ascii'))
        )
    except ValueError as ve:
        print(f"Error al procesar la clave privada: {ve}")
        exit(-1)
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        exit(-1)

    # Abre el archivo y lo guarda
    try:
        with open("../ficheros/priv_key.pem", "wb") as priv_key_file:
            priv_key_file.write(priv_pem)
    except FileNotFoundError:
        print("Error: no se encuentra el archivo")
        exit(-1)
    except IOError as e:
        print(f"Error al leer el archivo: {e}")
        exit(-1)


def cargar_priv_key():
    """Función que carga una clave privada a partir de un archivo"""
    try:
        with open("ficheros/priv_key.pem", "rb") as key_file:
            return serialization.load_pem_private_key(
                key_file.read(),
                password=bytes(generar_contrasena(), 'ascii')
            )
    except FileNotFoundError:
        print("Error: no se encuentra el archivo")
        exit(-1)
    except IOError as e:
        print(f"Error al leer el archivo: {e}")
        exit(-1)


def save_pub_key():
    """Función que serializa las claves y las guarda en un .pem"""
    private_key = cargar_priv_key()

    # Genera la clave pública a través de la privada
    public_key = private_key.public_key()

    # Serializa la clave publica y la guarda
    try:
        pub_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    except ValueError as ve:
        print(f"Error al procesar la clave pública: {ve}")
        exit(-1)
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        exit(-1)

    # Abre el archivo y lo guarda
    try:
        with open("../ficheros/pub_key.pem", "wb") as pub_key_file:
            pub_key_file.write(pub_pem)
    except FileNotFoundError:
        print("Error: no se encuentra el archivo")
        exit(-1)
    except IOError as e:
        print(f"Error al leer el archivo: {e}")
        exit(-1)


def cargar_pub_key():
    """Función que deserializa la clave publica"""
    # Abre el archivo y lo carga
    try:
        with open("../ficheros/pub_key.pem", "rb") as pub_key_file:
            return load_pem_public_key(pub_key_file.read())
    except FileNotFoundError:
        print("Error: no se encuentra el archivo")
    except IOError as e:
        print(f"Error al leer el archivo: {e}")

