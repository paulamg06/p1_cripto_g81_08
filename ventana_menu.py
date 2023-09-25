"""Fichero que contiene la ventana del menú principal"""
import tkinter as tk

class VentanaMenu(tk.Toplevel):
    """Clase que contiene la ventana del menú principal"""
    def __init__(self, app):
        super().__init__(app)
        self.app = app

        self.title("Menú de Selección")
        self.geometry("400x150")

        # Crear un contenedor Frame para los botones
        button_frame = tk.Frame(self)
        button_frame.pack(padx=20, pady=20)  # Ajusta el espaciado exterior

        # Crear botones y organizarlos en columnas
        button1 = tk.Button(button_frame, text="Tus cuentas atrás", command=self.opcion_ca)
        button2 = tk.Button(button_frame, text="Nuevo evento", command=self.opcion_nuevo_evento)
        button3 = tk.Button(button_frame, text="Cerrar sesión", command=self.opcion_ca)

        button1.grid(row=0, column=0, padx=10, pady=10)
        button2.grid(row=0, column=1, padx=10, pady=10)
        button3.grid(row=0, column=2, padx=10, pady=10)

    def opcion_ca(self):
        """Método que pasa a la ventana de cuentas atrás y destruye la ventana del menú"""
        self.app.abrir_cuenta_atras()
        self.app.ventana_menu = None
        self.destroy()

    def opcion_nuevo_evento(self):
        """Métodoo que pasa a la ventana de nuevo evento y destruye la ventana del menú"""
        self.app.abrir_nuevo_evento()
        self.app.ventana_menu = None
        self.destroy()