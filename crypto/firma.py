"""Fichero que contiene las funciones para la parte de la firma"""
import base64
import pickle

from cryptography import x509
from cryptography.exceptions import InvalidSignature

from crypto import gestion_claves, certificado

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


def firmar(message):
    """Función que devuelve la firma"""

    b64_message = pickle.dumps(message)

    # Pasa a bytes la info
    #message_str = " ".join(str(item) for item in message)  # Pasa la lista a cadena de caracteres
    #b64_message = message_str.encode("utf-8")  # Pasa la cadena a bytes


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
    guardar_firma(signature, b64_message)


def guardar_firma(signature, b64_message):
    """Función que guarda la firma"""
    # Crea un diccionario con la firma, el mensaje y el certificado
    ac_cert = certificado.cargar_certificado("ac1cert.pem")  # Certificado de AC
    a_cert = certificado.cargar_certificado("Acert.pem")

    firma = {
        "signature": signature,
        "b64_message": b64_message,
        "certificadoAC": ac_cert,
        "certificadoA": a_cert
    }

    # Guarda el diccionario en un fichero
    with open("ficheros/firma.sig", "wb") as signature_file:
        pickle.dump(firma, signature_file)


def cargar_firma():
    """Función que carga y devuelve la firma y el mensaje correspondiente"""
    # Abre el fichero donde se ha guardado la firma
    with open("ficheros/firma.sig", "rb") as signature_file:
        return pickle.load(signature_file)


def verificar_firma():
    """Función que verifica la firma del usuario con la clave de A"""
    # Carga la firma, el mensaje y el certificado
    firma = cargar_firma()
    signature, b64_message, cert_pem = firma["signature"], firma["b64_message"], firma["certificadoA"]
    print("s", signature, "\nb64", b64_message, "\ncert", cert_pem)

    # Carga el certificado desde la cadena PEM
    a_cert = x509.load_pem_x509_certificate(cert_pem)

    # Obtiene la clave pública del certificado
    public_key = a_cert.public_key()

    # Verifica con la clave publica
    public_key.verify(
        signature,
        b64_message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return firma


def verificar_certificado_A():
    """"""
    firma = cargar_firma()
    cert_a_pem = firma["certificadoA"]
    cert_ac_pem = firma["certificadoAC"]

    cert_ac = x509.load_pem_x509_certificate(cert_ac_pem)
    ac_pk = cert_ac.public_key()

    cert_check = x509.load_pem_x509_certificate(cert_a_pem)
    ac_pk.verify(
        cert_check.signature,
        cert_check.tbs_certificate_bytes,
        padding.PKCS1v15(),
        cert_check.signature_hash_algorithm
    )

    return cert_check

def verificar_certificado_AC():
    """"""
    firma = cargar_firma()
    cert_ac_pem = firma["certificadoAC"]

    cert_check = x509.load_pem_x509_certificate(cert_ac_pem)
    ac_pk = cert_check.public_key()
    ac_pk.verify(
        cert_check.signature,
        cert_check.tbs_certificate_bytes,
        padding.PKCS1v15(),
        cert_check.signature_hash_algorithm
    )

    return cert_check

