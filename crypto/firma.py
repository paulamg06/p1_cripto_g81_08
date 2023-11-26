"""Fichero que contiene las funciones para la parte de la firma"""
import pickle

from cryptography import x509

from crypto import gestion_claves, certificado

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


def firmar(message):
    """Función que devuelve la firma"""

    # Pasa a bytes la info
    message_str = " ".join(str(item) for item in message)  # Pasa la lista a cadena de caracteres
    b64_message = message_str.encode("utf-8")  # Pasa la cadena a bytes

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
    cert = certificado.cargar_certificado("Acert2.pem")  # Certificado de A

    firma = {
        "signature": signature,
        "b64_message": b64_message,
        "certificado": cert
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
    signature, b64_message, cert_pem = firma["signature"], firma["b64_message"], firma["certificado"]

    # Carga el certificado desde la cadena PEM
    cert = x509.load_pem_x509_certificate(cert_pem)

    # Obtiene la clave pública del certificado
    public_key = cert.public_key()

    # Si b64_message es una lista, se convierte a cadena de caracteres
    b64_message = " ".join(map(str, b64_message))

    # Verifica la clave publica
    public_key.verify(
        signature,
        b64_message.encode('utf-8'),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    # Verifica el siguiente nivel
    #verificar_firma_A(cert, b64_message, firma)
    return firma


def verificar_firma_A(cert, b64_message, firma):
    """Función que verifica la firma de A con su clave"""

    # Verifica la clave pública de A (nivel anterior) con la firma de A
    cert.public_key().verify(
        cert.signature,
        b64_message.encode('utf-8'),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    # Verifica el siguiente nivel
    verificar_firma2(cert, b64_message, firma)


def verificar_firma2(cert, b64_message, firma):
    """Función que verifica la firma de AC con la clave de A"""
    # Carga el certificado de AC
    ac_cert_pem = certificado.cargar_certificado("Acert.pem")

    # Carga el certificado desde la cadena PEM
    ac_cert = x509.load_pem_x509_certificate(ac_cert_pem)

    # Verifica la clave pública de A con la firma de AC
    cert.public_key().verify(
        ac_cert.signature,
        b64_message.encode('utf-8'),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    # Verifica el último nivel
    verificar_firma_AC(ac_cert, b64_message, firma)


def verificar_firma_AC(ac_cert, b64_message, firma):
    """Función que verifica la firma de AC con su clave"""
    # Verifica la clave pública de AC (nivel anterior) con la firma de AC
    ac_cert.public_key().verify(
        ac_cert.signature,
        b64_message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return firma  # Exito


if __name__ == '__main__':
    verificar_firma()
