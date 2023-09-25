"""Fichero que contiene la ventana del menú de cuenta atrás"""
import tkinter as tk

class VentanaCuentaAtras(tk.Toplevel):
    """Clase para configurar la ventana con las cuentas atrás del usuario"""
    def __init__(self, app):
        super().__init__(app)
        self.app = app

        #Configuramos la ventana
        self.title("Tus cuentas atrás")
        self.geometry("600x500")

        self.interfaz(self.app.usuario)

    def interfaz(self, usuario):
        """Método que configura la interfaz de la ventana"""

        self.bienvenida = tk.Label(self, text=f"{usuario}. Tus eventos:")
        self.bienvenida.place(x=20, y=5)

        self.titulo_c_a = tk.Label(self, text="Cuentas atrás:")
        self.titulo_c_a.place(x=300, y=5)

        #Estos textos se rellenan cuando se introduzcan nuevos eventos
        self.app.info_evento.place(x=20, y=35)
        self.app.info_cuenta_atras_evento.place(x=300, y=35)

        #Boton para volver al menú principal
        self.menu_principal = tk.Button(self, text="Abrir menú principal", command=self.app.abrir_menu_principal)
        self.menu_principal.place(x=20, y=110)
