"""Fichero que almacena los de los usuarios"""
class Evento():
    """Clase que almacena los eventos de los usuarios"""
    def __init__(self, nombre, fecha, hora):
        self.__nombre = nombre
        self.__fecha = fecha
        #Hay que modificar la hora para que sea opcional :)
        self.__hora = hora

    @property
    def nombre(self):
        return self.__nombre

    @property
    def fecha(self):
        """Verificamos que está en el formato correcto (dd/mm/aaaa)"""
        if len(self.__fecha) != 10:
            raise Exception("El formato de la fecha es dd/mm/aaaa")

        #Verificamos el año
        year = int(self.__fecha[6:])
        print(year)
        if year < 2023:
            raise Exception("Ese año ya ha pasado")

        month = int(self.__fecha[3:5])
        print(month)
        if month < 1 or month > 12:
            raise Exception("Introduce un mes válido")

        #Verificamos el dia
        dia = int(self.__fecha[:2])
        print(dia)
        if dia < 1 or dia > 31:
            raise Exception("Introduce un dia válido")


        return self.__fecha

    @property
    def hora(self):
        """Verificamos que está en el formato correcto (hh:mm)"""

        return self.__hora