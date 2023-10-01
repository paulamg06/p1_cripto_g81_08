"""Fichero que contiene la clase de la aplicación"""

from tkinter import ttk

from registro_usuarios import RegistroUsuarios
from gestion_evento import GestionEventos

from ventana_inicio_sesion import VentanaInicioSesion
from ventana_menu import VentanaMenu
from ventana_cuenta_atras import VentanaCuentaAtras
from ventana_nuevo_evento import VentanaNuevoEvento
from ventana_registro import VentanaRegistro
from ventana_borrar_evento import VentanaBorrarEvento


"""Recordatorio: ttk.Label para los textos, ttk.Entry para las cajas, ttk.Bottom para los botones.
Siempre hay que poner el parent"""

class Aplicacion(ttk.Frame):
    """Clase que contiene toda la estructura de la apliacion"""
    def __init__(self, root, db_file):
        super().__init__()
        self.root = root
        self.root.withdraw()

        #registro usuarios
        self.registro = RegistroUsuarios(db_file)
        self.gestion = GestionEventos(db_file)

        self.usuario = "" #La variable se almacena en la clase de registro

        #Textos que se van a modificar en cuanto se añadan eventos
        self.info_evento = ttk.Label(self, text="")
        self.info_cuenta_atras_evento = ttk.Label(self, text="")

        self.root = None
        self.ventana_menu = None
        self.ventana_cuenta_atras = None
        self.ventana_nuevo_evento = None
        self.ventana_registro_usuario = None
        self.ventana_inicio_sesion = None

        #Ventana de inicio de sesion
        self.abrir_inicio_sesion()

    def abrir_inicio_sesion(self):
        """Método que abre la ventana para el inicio de sesión"""
        if self.ventana_registro_usuario:
            self.ventana_registro_usuario.destroy()

        self.ventana_inicio_sesion = VentanaInicioSesion(self, self.registro)


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


    def abrir_registro_usuario(self):
        """Método que abre la ventana para registrar el usuario"""

        self.ventana_registro_usuario = VentanaRegistro(self, self.registro)


    def abrir_borrar_evento(self):
        """Método que abre la ventana para borrar un evento"""
        if self.ventana_cuenta_atras:
            self.ventana_cuenta_atras.destroy()

        self.ventana_borrar_evento = VentanaBorrarEvento(self)
