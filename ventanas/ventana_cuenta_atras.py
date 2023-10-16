"""Fichero que contiene la ventana del menú de cuenta atrás"""
import tkinter as tk

class VentanaCuentaAtras(tk.Toplevel):
    """Clase para configurar la ventana con las cuentas atrás del usuario"""
    def __init__(self, app):
        super().__init__(app)
        self.app = app

        #Configuramos la ventana
        self.title("Tus eventos")
        self.geometry("600x500")

        self.info_eventos = {} #Diccionario con los textos de los eventos

        self.interfaz(self.app.usuario)

    def interfaz(self, usuario):
        """Método que configura la interfaz de la ventana"""
        #Encabezados
        self.bienvenida = tk.Label(self, text="Tus cuentas atrás:")
        self.bienvenida.place(x=20, y=5)

        #Información de los eventos y el encabezado
        self.imprimir_eventos(usuario)

        #Boton para volver al menú principal
        self.menu_principal = tk.Button(self, text="Abrir menú principal", command=self.app.abrir_menu_principal)
        self.menu_principal.place(x=20, y=110)
        self.borrar_evento = tk.Button(self, text="Borrar un evento", command=self.app.abrir_borrar_evento)
        self.borrar_evento.place(x=20, y=140)


    def imprimir_eventos(self, usuario):
        #Obtenemos la lista con todos los eventos del usuario
        lista_eventos = self.app.gestion.obtener_eventos(usuario, self.app.data_key)
        y_actual = 30

        """El nombre del evento está en la posición 2,
        la fecha del evento está en la posición 3 y
        la cuenta atrás del evento está en la posición 4."""

        #Recorremos los eventos
        for evento in lista_eventos:
            #Almacenamos cada texto en una entrada distinta del diccionario
            self.info_eventos[evento[0]] = tk.Label(self, text=f"{evento[0]}, {evento[1]}. Queda {evento[2]}")
            self.info_eventos[evento[0]].place(x=20, y=y_actual)

            #Subimos la posición de la y
            y_actual += 20
