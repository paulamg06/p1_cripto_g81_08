"""Fichero que almacena los de los usuarios"""
from datetime import datetime
from cuenta_atras import CuentaAtras

class Evento():
    """Clase que almacena los eventos de los usuarios"""
    def __init__(self, nombre, fecha, hora):
        self.__nombre = nombre
        self.__fecha = self.paso_fecha(fecha, hora)
        self.cuenta_atras = self.hacer_cuenta_atras()

    def paso_fecha(self, fecha, hora):
        """Función que pasa la fecha a datetime"""
        date = fecha + ", " + hora
        return datetime.strptime(date, '%d-%m-%Y, %H:%M')


    def paso_unidades_fecha(self, dias):
        """Función que pasa la diferencia a años, meses y días"""
        years = dias // 365
        months = (dias % 365) // 30
        days = (dias % 365 ) % 30
        return years, months, days

    def paso_unidades_hora(self, seconds):
        """Función que pasa los segundos a horas y minutos"""
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60

        return hours, minutes


    def hacer_cuenta_atras(self):
        """Función que hace la cuenta atrás del evento"""
        #Obtenemos la fecha actual
        fecha_actual = datetime.now()
        diferencia = self.__fecha - fecha_actual

        years, days, months = self.paso_unidades_fecha(diferencia.days)

        hours, minutes = self.paso_unidades_hora(diferencia.seconds)

        return str(CuentaAtras(years, days, months, hours, minutes))


    @property
    def nombre(self):
        return self.__nombre

    @property
    def fecha(self):
        return self.__fecha

    @property
    def hora(self):
        return self.__hora