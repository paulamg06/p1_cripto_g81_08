"""Fichero que contiene la clase de la aplicación"""
from tkinter import ttk
from evento import Evento

"""Recordatorio: ttk.Label para los textos, ttk.Entry para las cajas, ttk.Bottom para los botones.
Siempre hay que poner el parent"""

class Aplicacion(ttk.Frame):
    """Clase que contiene toda la estructura de la apliacion"""
    def __init__(self, parent):
        super().__init__(parent)

        #Para ir imprimiendo los últimos eventos (esto ya lo cambiaremos para que no se sobreescriban)
        self.contador = 0

        self.scroll = ttk.Scrollbar(parent, orient="vertical")
        self.scroll.place(x=560, heigh=500, width=50)

        #Lista de eventos
        self.eventos = []
        self.cuenta_atras = []

        'Texto'
        self.bienvenida = ttk.Label(parent, text="Tus eventos:")
        self.bienvenida.place(x=20, y=5)

        self.titulo_c_a = ttk.Label(parent, text="Cuentas atrás:")
        self.titulo_c_a.place(x=300, y=5)

        self.info_evento = ttk.Label(parent, text="")
        self.info_evento.place(x=20, y=35)

        self.info_cuenta_atras_evento = ttk.Label(parent, text="")
        self.info_cuenta_atras_evento.place(x=300, y=35)

        self.separador = ttk.Label(parent, text="-----------------------------------------------------")
        self.separador.place(x=0, y=55)

        self.texto_nombre = ttk.Label(parent, text="Nombre del evento: ")
        self.texto_nombre.place(x=20, y=75)

        self.texto_fecha = ttk.Label(parent, text="Fecha del evento (dd-mm-aaaa): ")
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

    def comprobar_fecha(self, fecha:str):
        """Función que verifica que la fecha está en el formato correcto (dd-mm-aaaa)"""

        if len(fecha) != 10:
            raise Exception("El formato de la fecha es dd-mm-aaaa")

        #Verificamos el año
        year = int(fecha[6:])
        #print(year)
        if year < 0:
            raise Exception("Introduce un año válido")

        #Verificamos el mes
        month = int(fecha[3:5])
        #print(month)
        if month < 1 or month > 12:
            raise Exception("Introduce un mes válido")

        if month == 2:
            limite_dias = 28
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            limite_dias = 31
        else:
            limite_dias = 30

        #Verificamos el dia
        dia = int(fecha[:2])
        #print(dia)
        if dia < 1 or dia > limite_dias:
            raise Exception("Introduce un dia válido")


    def comprobar_hora(self, hora:str):
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

        #Si no se introduce ningún nombre ni fecha, no hace nada
        if not nombre or not fecha:
            return None

        #Comprobamos el formato de la fecha
        self.comprobar_fecha(fecha)

        #La hora por defecto es 9:00
        if not hora:
            self.eventos.append(Evento(nombre, fecha, "9:00"))
        else:
            #Comprobamos el formato de la hora
            self.comprobar_hora(hora)
            self.eventos.append(Evento(nombre, fecha, hora))

        #Guardamos la cuenta atrás
        self.cuenta_atras.append(self.eventos[self.contador].cuenta_atras)

        self.info_evento.config(text=f"{self.eventos[self.contador].nombre}: {self.eventos[self.contador].fecha}")
        self.info_cuenta_atras_evento.config(text=self.cuenta_atras[self.contador])
        self.contador += 1