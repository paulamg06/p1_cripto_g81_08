"""Fichero que contiene la ventana del menú de cuenta atrás"""
import tkinter as tk
from tkinter import messagebox

from cryptography.exceptions import InvalidSignature

from crypto import firma


class VentanaCuentaAtras(tk.Toplevel):
    """Clase para configurar la ventana con las cuentas atrás del usuario"""

    def __init__(self, app):
        super().__init__(app)
        self.app = app

        # Configura la ventana
        self.title("Tus eventos")
        self.geometry("600x500")

        self.info_eventos = {}  # Diccionario con los textos de los eventos

        self.interfaz(self.app.usuario)

    def interfaz(self, usuario):
        """Método que configura la interfaz de la ventana"""
        # Encabezados
        self.bienvenida = tk.Label(self, text="Tus cuentas atrás:")
        self.bienvenida.place(x=20, y=5)

        # Información de los eventos y el encabezado
        self.imprimir_eventos(usuario)

        # Boton para volver al menú principal
        self.menu_principal = tk.Button(self, text="Volver atrás", command=self.app.abrir_menu_principal)
        self.menu_principal.place(x=20, y=420)
        self.borrar_evento = tk.Button(self, text="Borrar un evento", command=self.app.abrir_borrar_evento)
        self.borrar_evento.place(x=20, y=450)

    def verificar_firma(self):
        """Método que verifica la firma y muestra el resultado"""
        try:
            signature = firma.verificar_firma()
            mensaje_s = "Verificación de la firma correcto\n" + str(signature)
            messagebox.showinfo("Éxito", mensaje_s)
        except InvalidSignature as e:
            messagebox.showerror("Error Firma", "Error al verificar la firma del usuario")
            self.app.abrir_menu_principal()

        try:
            cert_a = firma.verificar_certificado_A()
            mensaje_a = "Verificación del certificado del usuario correcto\n" + str(cert_a)
            messagebox.showinfo("Éxito", mensaje_a)
        except Exception as e:
            messagebox.showerror("Error CertA", "Error al verificar el certificado del usuario")
            self.app.abrir_menu_principal()

        try:
            cert_ac = firma.verificar_certificado_AC()
            mensaje_ac = "Verificación del certificado de la Autoridad de Certificación correcto\n" + str(cert_ac)
            messagebox.showinfo("Éxito", mensaje_ac)
        except Exception as e:
            messagebox.showerror("Error CertAC", "Error al verificar el certificado de la Autoridad de Certificación")
            self.app.abrir_menu_principal()


    def imprimir_eventos(self, usuario):
        """Método que imprime los eventos en la interfaz"""
        # Verifica la firma
        self.verificar_firma()

        # Obtiene la lista con todos los eventos del usuario
        lista_eventos = self.app.gestion.obtener_eventos(usuario, self.app.data_key)
        y_actual = 30

        """El nombre del evento está en la posición 2,
        la fecha del evento está en la posición 3 y
        la cuenta atrás del evento está en la posición 4."""

        # Recorremos los eventos
        for evento in lista_eventos:
            # Almacenamos cada texto en una entrada distinta del diccionario
            self.info_eventos[evento[0]] = tk.Label(self, text=f"{evento[0]}, {evento[1]}. Queda {evento[2]}")
            self.info_eventos[evento[0]].place(x=20, y=y_actual)

            # Subimos la posición de la y
            y_actual += 20
