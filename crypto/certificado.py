"""Fichero que contiene las funciones para la parte de certificación"""
from crypto import gestion_claves

from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization


def crear_csr():
    """Función que crea la solicitud de certificado"""
    # Carga la clave privada del archivo
    private_key = gestion_claves.cargar_priv_key()

    # Crea el csr
    csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
        # Datos de la autoridad de certificación
        x509.NameAttribute(NameOID.COUNTRY_NAME, "ES"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "MADRID"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "UC3M"),
        x509.NameAttribute(NameOID.ORGANIZATION_UNIT_NAME, "INF"),
        x509.NameAttribute(NameOID.COMMON_NAME, "AC1"),
    ])).add_extension(
        x509.SubjectAlternativeName([
            x509.DNSName("AC1.com"),
            x509.DNSName("www.AC1.com"),
        ]),
        critical=False,
    # El csr se firma con la clave privada
    ).sign(private_key, hashes.SHA256())

    # Guarda el csr en un fichero
    with open("../ficheros/csr.pem", "wb") as csr_file:
        csr_file.write(csr.public_bytes(serialization.Encoding.PEM))

def cargar_certificado():
    """Función que carga el certificado guardado"""
    # Abre el certificado
    with open("../ficheros/Acert2.pem") as cert_file:
        pem_data = cert_file.read()

    # Devuelve el certificado
    certf = x509.load_pem_x509_certificate(bytes(pem_data, 'utf-8'))
    print(certf.public_key())

if __name__ == '__main__':
    cargar_certificado()
