"""Fichero que contiene la clase de la aplicación"""
from tkinter import ttk
from login_window import LoginWindow
from ventana_menu import VentanaMenu
from ventana_ca import VentanaCuentaAtras
from ventana_nuevo_evento import VentanaNuevoEvento

"""Recordatorio: ttk.Label para los textos, ttk.Entry para las cajas, ttk.Bottom para los botones.
Siempre hay que poner el parent"""

class Aplicacion(ttk.Frame):
    """Clase que contiene toda la estructura de la apliacion"""
    def __init__(self, root):
        super().__init__()
        self.root = root
        # Le damos un titulo al programa
        self.root.title("Cuenta atras")

        self.usuario = ""

        self.ventana_menu = None
        self.ventana_cuenta_atras = None
        self.ventana_nuevo_evento = None

        #Ventana de inicio de sesion
        self.inicio_sesion = LoginWindow(self)

    def abrir_menu_principal(self):
        """Método que se ejecuta tras un inicio de sesión correcto y llama a la ventana principal"""
        # Cerramos las otras ventanas en caso de que estuvieran abiertas
        if self.ventana_nuevo_evento:
            self.ventana_nuevo_evento.destroy()
        if self.ventana_cuenta_atras:
            self.ventana_cuenta_atras.destroy()

        # Abrimos la ventana del menú
        self.ventana_menu = VentanaMenu(self)


    def abrir_cuenta_atras(self):
        """Método que se ejecuta tras seleccionar su opción en el menú"""
        # Cerramos la ventana del menú
        if self.ventana_menu:
            self.ventana_menu.destroy()

        #Abrimos la ventana de cuenta atras
        self.ventana_cuenta_atras = VentanaCuentaAtras(self)

    def abrir_nuevo_evento(self):
        """Método que abre la ventana para introducir nuevos eventos"""
        # Cerramos la ventana del menú
        if self.ventana_menu:
            self.ventana_menu.destroy()

        # Abrimos la ventana de nuevo evento
        self.ventana_nuevo_evento = VentanaNuevoEvento(self)
