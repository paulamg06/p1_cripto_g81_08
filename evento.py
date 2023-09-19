"""Fichero que almacena los de los usuarios"""
class Evento():
    """Clase que almacena los eventos de los usuarios"""
    def __init__(self, nombre, fecha, hora):
        self.nombre = nombre
        self.fecha = fecha
        #Hay que modificar la hora para que sea opcional :)
        self.hora = hora
