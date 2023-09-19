"""Fichero que contiene la clase de la aplicación"""
from tkinter import ttk
from evento import Evento

"""Recordatorio: ttk.Label para los textos, ttk.Entry para las cajas, ttk.Bottom para los botones.
Siempre hay que poner el parent"""

class Aplicacion(ttk.Frame):
    """Clase que contiene toda la estructura de la apliacion"""
    def __init__(self, parent):
        super().__init__(parent)

        self.scroll = ttk.Scrollbar(parent, orient="vertical")
        self.scroll.place(x=560, heigh=500, width=50)

        #Lista de eventos
        self.eventos = []

        'Texto'
        self.bienvenida = ttk.Label(parent, text="Tus eventos: ")
        self.bienvenida.place(x=20, y=5)

        self.info_evento = ttk.Label(parent, text="nombre, dd/mm/aaaa, hh:mm")
        self.info_evento.place(x=20, y=35)

        self.separador = ttk.Label(parent, text="-----------------------------------------------------")
        self.separador.place(x=0, y=55)

        self.texto_nombre = ttk.Label(parent, text="Nombre del evento: ")
        self.texto_nombre.place(x=20, y=75)

        self.texto_fecha = ttk.Label(parent, text="Fecha del evento (dd/mm/aaaa): ")
        self.texto_fecha.place(x=20, y=110)

        self.texto_hora = ttk.Label(parent, text="*Hora del evento (hh:mm): ")
        self.texto_hora.place(x=20, y=145)


        'Cuadros'
        self.cuadro_nombre = ttk.Entry(parent)
        self.cuadro_nombre.place(x=130, y=75)

        self.cuadro_fecha = ttk.Entry(parent)
        self.cuadro_fecha.place(x=200, y=110, width=70)

        self.cuadro_hora = ttk.Entry(parent)
        self.cuadro_hora.place(x=170, y=145, width=50)

        'Botones'
        self.introducir = ttk.Button(parent, text="Nuevo evento", command=self.crear_nuevo_evento)
        self.introducir.place(x=20, y=180)

    def crear_nuevo_evento(self):
        """Función que crea una nueva instancia evento"""
        nombre = str(self.cuadro_nombre.get())
        fecha = str(self.cuadro_fecha.get())
        hora = str(self.cuadro_hora.get())

        #Si no se introduce ningún nombre ni fecha, no hace nada
        if not nombre or not fecha:
            return None

        if not hora:
            self.eventos.append(Evento(nombre, fecha, "9:00"))
        else:
            self.eventos.append(Evento(nombre, fecha, hora))

        self.info_evento.config(text=f"Evento: {self.eventos[0].nombre}, {self.eventos[0].fecha}, {self.eventos[0].hora}")