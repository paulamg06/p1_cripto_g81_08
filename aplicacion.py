"""Fichero que contiene la clase de la aplicación"""
from tkinter import ttk
from evento import Evento

"""Recordatorio: ttk.Label para los textos, ttk.Entry para las cajas, ttk.Bottom para los botones.
Siempre hay que poner el parent"""

class Aplicacion(ttk.Frame):
    """Clase que contiene toda la estructura de la apliacion"""
    def __init__(self, parent):
        super().__init__(parent)

        #Lista de eventos
        self.eventos = []

        'Texto'
        self.bienvenida = ttk.Label(parent, text="Tus cuenta atrás: ")
        self.bienvenida.place(x=20, y=5)

        self.texto_nombre = ttk.Label(parent, text="Nombre del evento: ")
        self.texto_nombre.place(x=20, y=35)

        self.texto_fecha = ttk.Label(parent, text="Fecha del evento: ")
        self.texto_fecha.place(x=20, y=70)

        self.texto_hora = ttk.Label(parent, text="Hora del evento (opcional): ")
        self.texto_hora.place(x=20, y=105)

        'Cuadros'
        self.cuadro_nombre = ttk.Entry(parent)
        self.cuadro_nombre.place(x=170, y=35)

        self.cuadro_fecha = ttk.Entry(parent)
        self.cuadro_fecha.place(x=170, y=70)

        self.cuadro_hora = ttk.Entry(parent)
        self.cuadro_hora.place(x=170, y=105)

        'Botones'
        self.introducir = ttk.Button(parent, text="Nuevo evento")
        self.introducir.place(x=20, y=140)

    def crear_nuevo_evento(self):
        """Función que crea una nueva instancia evento"""
        nombre = self.cuadro_nombre.get()
        fecha = self.cuadro_fecha.get()
        hora = self.cuadro_hora.get()

        if not hora:
            self.eventos.append(Evento(nombre, fecha, "9:00"))
        else:
            self.eventos.append(Evento(nombre, fecha, hora))
