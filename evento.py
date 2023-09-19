"""Fichero que almacena los de los usuarios"""
from datetime import datetime

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


    def hacer_cuenta_atras(self):
        """Función que hace la cuenta atrás del evento"""
        #Obtenemos la fecha actual
        fecha_actual = datetime.now()
        diferencia = self.__fecha - fecha_actual

        return diferencia



    @property
    def nombre(self):
        return self.__nombre

    @property
    def fecha(self):
        return self.__fecha

    @property
    def hora(self):
        return self.__hora