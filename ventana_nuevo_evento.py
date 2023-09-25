"""Fichero que contiene la ventana para los nuevos eventos"""
import tkinter as tk
from evento import Evento

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
        self.eventos = []
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
        self.introducir = tk.Button(self, text="Nuevo evento", command=self.crear_nuevo_evento)
        self.introducir.place(x=20, y=125)

        # Boton para volver al menú principal
        self.menu_principal = tk.Button(self, text="Abrir menú principal", command=self.app.abrir_menu_principal)
        self.menu_principal.place(x=250, y=160)

    def comprobar_fecha(self, fecha: str):
        """Función que verifica que la fecha está en el formato correcto (dd-mm-aaaa)"""

        if len(fecha) != 10:
            raise Exception("El formato de la fecha es dd-mm-aaaa")

        # Verificamos el año
        year = int(fecha[6:])
        # print(year)
        if year < 0:
            raise Exception("Introduce un año válido")

        # Verificamos el mes
        month = int(fecha[3:5])
        # print(month)
        if month < 1 or month > 12:
            raise Exception("Introduce un mes válido")

        if month == 2:
            limite_dias = 28
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            limite_dias = 31
        else:
            limite_dias = 30

        # Verificamos el dia
        dia = int(fecha[:2])
        # print(dia)
        if dia < 1 or dia > limite_dias:
            raise Exception("Introduce un dia válido")

    def comprobar_hora(self, hora: str):
        """Función que verifica que está en el formato correcto (HH:MM)"""

        if len(hora) != 5:
            raise Exception("El formato de hora debe ser hh:mm")

        hour = int(hora[:2])
        if hour < 0 or hour > 23:
            raise Exception("Introduce una hora válida")

        minute = int(hora[3:])
        if minute < 0 or minute > 59:
            raise Exception("Introduce unos minutos válidos")

    def crear_nuevo_evento(self):
        """Función que crea una nueva instancia evento"""
        nombre = str(self.cuadro_nombre.get())
        fecha = str(self.cuadro_fecha.get())
        hora = str(self.cuadro_hora.get())

        # Si no se introduce ningún nombre ni fecha, no hace nada
        if not nombre or not fecha:
            return None

        # Comprobamos el formato de la fecha
        self.comprobar_fecha(fecha)

        # La hora por defecto es 9:00
        if not hora:
            self.eventos.append(Evento(nombre, fecha, "9:00"))
        else:
            # Comprobamos el formato de la hora
            self.comprobar_hora(hora)
            self.eventos.append(Evento(nombre, fecha, hora))

        # Guardamos la cuenta atrás
        self.cuenta_atras.append(self.eventos[self.contador].cuenta_atras)

        self.info_evento.config(text=f"{self.eventos[self.contador].nombre}: {self.eventos[self.contador].fecha}")
        self.info_cuenta_atras_evento.config(text=self.cuenta_atras[self.contador])
        self.contador += 1