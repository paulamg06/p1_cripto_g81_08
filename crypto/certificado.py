"""Fichero que contiene las funciones para la parte de certificación"""
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from crypto import firma

def crear_csr():
    """Función que crea la solicitud de certificado"""
    private_key = firma.cargar_priv_key()

    csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
        # Provide various details about who we are.
        x509.NameAttribute(NameOID.COUNTRY_NAME, "ES"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "MADRID"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "UC3M"),
        x509.NameAttribute(NameOID.ORGANIZATION_UNIT_NAME, "INF"),
        x509.NameAttribute(NameOID.COMMON_NAME, "AC1"),
    ])).add_extension(
        x509.SubjectAlternativeName([
            # Describe what sites we want this certificate for.
            x509.DNSName("AC1.com"),
            x509.DNSName("www.AC1.com"),
        ]),
        critical=False,
        # Sign the CSR with our private key.
    ).sign(private_key, hashes.SHA256())
    # Write our CSR out to disk.
    with open("../ficheros/csr.pem", "wb") as f:
        f.write(csr.public_bytes(serialization.Encoding.PEM))

if __name__ == '__main__':
    crear_csr()