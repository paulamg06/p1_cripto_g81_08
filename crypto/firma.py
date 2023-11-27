"""Fichero que contiene las funciones para la parte de la firma"""
import pickle

from cryptography import x509

from crypto import gestion_claves, certificado

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


def firmar(message):
    """Función que devuelve la firma"""
    # Pasa el mensaje a bytes
    b64_message = pickle.dumps(message)

    # Carga la clave privada
    private_key = gestion_claves.cargar_priv_key()

    # Firma con la clave privada
    signature = private_key.sign(
        b64_message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    # Guarda la firma
    guardar_firma(signature, b64_message)


def guardar_firma(signature, b64_message):
    """Función que guarda la firma, el mensaje, el certificado del usuario y el de la AC en un fichero"""
    # Crea un diccionario con la firma, el mensaje y el certificado
    ac_cert = certificado.cargar_certificado("ac1cert.pem")  # Certificado de AC
    a_cert = certificado.cargar_certificado("Acert.pem")  # Certificado del usuario

    dic_file = {
        "signature": signature,
        "b64_message": b64_message,
        "certificadoAC": ac_cert,
        "certificadoA": a_cert
    }

    # Guarda el diccionario en un fichero
    with open("ficheros/firma.sig", "wb") as signature_file:
        pickle.dump(dic_file, signature_file)


def cargar_firma():
    """Función que carga y devuelve la firma y el mensaje correspondiente"""
    # Abre el fichero donde se ha guardado la firma
    with open("ficheros/firma.sig", "rb") as signature_file:
        return pickle.load(signature_file)


def verificar_firma():
    """Función que verifica la firma del usuario con la clave de A"""
    # Carga la firma, el mensaje y el certificado
    dic_file = cargar_firma()
    firma, b64_message, cert_pem = dic_file["signature"], dic_file["b64_message"], dic_file["certificadoA"]

    # Carga el certificado desde la cadena PEM
    a_cert = x509.load_pem_x509_certificate(cert_pem)

    # Obtiene la clave pública del certificado
    public_key = a_cert.public_key()

    # Verifica con la clave publica
    public_key.verify(
        firma,
        b64_message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    # Si va bien, devuelve la firma
    return firma


def verificar_certificado_A():
    """Función que verifica el certificado del usuario"""
    dic_file = cargar_firma()

    # Carga el certificado del usuario
    cert_a_pem = dic_file["certificadoA"]
    cert_check = x509.load_pem_x509_certificate(cert_a_pem)

    # Carga el certificado de la AC y obtiene su clave publica
    cert_ac_pem = dic_file["certificadoAC"]
    cert_ac = x509.load_pem_x509_certificate(cert_ac_pem)
    ac_pk = cert_ac.public_key()

    # Verifica el certificado con la clave pública de la AC
    ac_pk.verify(
        cert_check.signature,
        cert_check.tbs_certificate_bytes,
        padding.PKCS1v15(),
        cert_check.signature_hash_algorithm
    )

    # Si va bien, devuelve el certificado del usuario
    return cert_check


def verificar_certificado_AC():
    """Función que verifica el certificado de la AC"""
    dic_file = cargar_firma()

    # Carga el certificado de la AC y guarda su clave publica
    cert_ac_pem = dic_file["certificadoAC"]
    cert_check = x509.load_pem_x509_certificate(cert_ac_pem)
    ac_pk = cert_check.public_key()

    # Verifica con su clave pública
    ac_pk.verify(
        cert_check.signature,
        cert_check.tbs_certificate_bytes,
        padding.PKCS1v15(),
        cert_check.signature_hash_algorithm
    )

    # Si va bien, devuelve el certificado de la AC
    return cert_check
