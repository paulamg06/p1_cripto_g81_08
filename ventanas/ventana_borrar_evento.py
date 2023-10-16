"""Fichero que contiene la ventana para borrar eventos"""
import tkinter as tk

class VentanaBorrarEvento(tk.Toplevel):
    """Clase que configura la ventana para borrar eventos"""
    def __init__(self, app):
        super().__init__(app)
        self.app = app

        self.usuario = self.app.usuario

        #Configuramos la ventana
        # Configuramos la ventana
        self.title("Tus eventos")
        self.geometry("600x500")

        #Diccionario que almacena los eventos
        self.botones_eventos = {}
        #Inicializamos una variable que vaya a guardar cada evento
        self.evento_actual = None

        self.interfaz(self.usuario)

    def interfaz(self, usuario):
        """Método que configura la ventana"""
        # Obtenemos la lista con todos los eventos del usuario
        lista_eventos = self.app.gestion.obtener_eventos(usuario, self.app.data_key)
        y_actual = 30

        """El nombre del evento está en la posición 2,
        la fecha del evento está en la posición 3 y
        la cuenta atrás del evento está en la posición 4."""

        # Recorremos los eventos
        for evento in lista_eventos:
            self.evento_actual = evento
            # Almacenamos cada texto en una entrada distinta del diccionario
            self.botones_eventos[evento[0]] = tk.Button(self, text=f"{evento[0]}, {evento[1]}", command=self.borrar_evento)
            self.botones_eventos[evento[0]].place(x=20, y=y_actual)

            # Subimos la posición de la y
            y_actual += 30

    def borrar_evento(self):
        """Método que borra el evento"""
        self.app.gestion.borrar_evento(self.evento_actual, self.usuario, self.app.data_key)
        #Cerramos la ventana después de haber borrado el evento
        self.app.abrir_cuenta_atras()
        self.destroy()
