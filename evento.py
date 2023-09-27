"""Fichero que almacena los de los usuarios"""
from datetime import datetime
from cuenta_atras import CuentaAtras

class Evento:
    """Clase que almacena los eventos de los usuarios"""
    def __init__(self, nombre, fecha, hora):
        self.nombre = nombre
        self.fecha = self.paso_fecha(fecha, hora)
        self.cuenta_atras = self.hacer_cuenta_atras()

    def paso_fecha(self, fecha, hora):
        """Función que pasa la fecha a datetime"""
        date = fecha + ", " + hora
        return datetime.strptime(date, '%d-%m-%Y, %H:%M')

    def calculo_anios(self, days):
        """Función que calcula los años"""
        return days % 365

    def paso_unidades_hora(self, seconds):
        """Función que pasa los segundos a horas y minutos"""
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60

        return hours, minutes

    def hacer_cuenta_atras(self):
        """Función que hace la cuenta atrás del evento"""
        #Obtenemos la fecha actual
        fecha_actual = datetime.now()
        diferencia = self.fecha - fecha_actual

        #Si es negativo, no deja
        if diferencia.days < 0 or diferencia.seconds < 0:
            return None

        #Si queda más de 1 año, se muestra como +1
        if diferencia.days > 365:
            years = self.calculo_anios(diferencia.days)
            return str(CuentaAtras(years, None, None, None))

        #Si queda menos de 1 año, se muestra toda la info
        hours, minutes = self.paso_unidades_hora(diferencia.seconds)
        return str(CuentaAtras(None, diferencia.days, hours, minutes))
