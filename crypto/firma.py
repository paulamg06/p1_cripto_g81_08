"""Fichero que contiene las funciones para la parte de la firma"""
import pickle
from db.gestion_evento import GestionEventos
from crypto import gestion_claves, certificado

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


def firmar(db_file, usuario, data_key):
    """Función que devuelve la firma"""
    # Carga lo que se quiere firmar
    gestion_evento = GestionEventos(db_file)
    message = gestion_evento.obtener_eventos(usuario, data_key)

    # Pasa a bytes la info
    b64_message = bytes(message, "ascii")

    # Carga la clave privada
    private_key = gestion_claves.cargar_priv_key()

    # Firma y se guarda
    signature = private_key.sign(
        b64_message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    guardar_firma(signature, message)


def guardar_firma(signature, b64_message):
    """Función que guarda la firma"""
    # Crea un diccionario con la firma, el mensaje y el certificado
    cert = certificado.cargar_certificado()
    firma = {
        "signature": signature,
        "b64_message": b64_message,  ## También hay que guardar el certificado
        "certificado": cert
    }

    # Guarda el diccionario en un fichero
    with open("../ficheros/firma.sig", "wb") as signature_file:
        pickle.dump(firma, signature_file)


def cargar_firma():
    """Función que carga y devuelve la firma y el mensaje correspondiente"""

    with open("../ficheros/firma.sig", "rb") as signature_file:
        firma = pickle.load(signature_file)

    return firma["signature"], firma["b64_message"], firma["certificado"]


def verificar_firma():
    """Función que verifica la firma"""

    # Carga la firma, el mensaje y el certificado
    signature, b64_message, cert = cargar_firma()

    public_key = cert.public_key()

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



if __name__ == '__main__':
    verificar_firma()
