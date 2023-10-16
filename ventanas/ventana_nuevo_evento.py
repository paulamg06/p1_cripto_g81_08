"""Fichero que contiene la ventana para los nuevos eventos"""
import tkinter as tk
from objetos.evento import Evento

class VentanaNuevoEvento(tk.Toplevel):
    """Clase que genera la ventana para crear nuevos eventos"""
    def __init__(self, app):
        super().__init__(app)
        self.app = app

        #Configuramos la ventana
        self.title("Crear un nuevo evento")
        self.geometry("400x200")

        self.interfaz()

    def interfaz(self):
        """Método que configura la interfaz de la ventana"""
        self.scroll = tk.Scrollbar(self, orient="vertical")
        self.scroll.place(x=560, heigh=500, width=50)

        # Lista de eventos
        self.app.eventos = []
        self.cuenta_atras = []

        'Texto'
        self.texto_nombre = tk.Label(self, text="Nombre del evento: ")
        self.texto_nombre.place(x=20, y=20)

        self.texto_fecha = tk.Label(self, text="Fecha del evento (dd-mm-aaaa): ")
        self.texto_fecha.place(x=20, y=55)

        self.texto_hora = tk.Label(self, text="*Hora del evento (hh:mm): ")
        self.texto_hora.place(x=20, y=90)

        'Cuadros'
        self.cuadro_nombre = tk.Entry(self)
        self.cuadro_nombre.place(x=130, y=20)

        self.cuadro_fecha = tk.Entry(self)
        self.cuadro_fecha.place(x=200, y=55, width=70)

        self.cuadro_hora = tk.Entry(self)
        self.cuadro_hora.place(x=170, y=90, width=50)

        'Botones'
        self.introducir = tk.Button(self, text="Crear evento", command=self.crear_nuevo_evento)
        self.introducir.place(x=20, y=125)

        # Boton para volver al menú principal
        self.menu_principal = tk.Button(self, text="Abrir menú principal", command=self.app.abrir_menu_principal)
        self.menu_principal.place(x=250, y=160)


    def crear_nuevo_evento(self):
        """Función que crea una nueva instancia evento"""
        nombre = str(self.cuadro_nombre.get())
        fecha = str(self.cuadro_fecha.get())
        hora = str(self.cuadro_hora.get())

        # Si no se introduce ningún nombre ni fecha, no hace nada
        if not nombre or not fecha:
            return None

        # La hora por defecto es 9:00
        if not hora:
            nuevo_evento = Evento(nombre, fecha, "9:00")
        else:
            nuevo_evento = Evento(nombre, fecha, hora)

        self.app.gestion.crear_evento(nuevo_evento, self.app.usuario, self.app.data_key)
