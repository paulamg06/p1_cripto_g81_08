"""Fichero que contiene la ventana del menú principal"""
import tkinter as tk

class VentanaMenu(tk.Toplevel):
    """Clase que contiene la ventana del menú principal"""
    def __init__(self, app, usuario):
        super().__init__(app)
        self.app = app
        self.usuario = usuario

        self.title("Menú de Selección")
        self.geometry("300x150")

        # Crear un contenedor Frame para los botones
        button_frame = tk.Frame(self)
        button_frame.pack(padx=20, pady=20)  # Ajusta el espaciado exterior

        # Crear botones y organizarlos en columnas
        button1 = tk.Button(button_frame, text="Cuenta atrás", command=self.opcion1)
        button2 = tk.Button(button_frame, text="Opción 2", command=self.opcion1)
        button3 = tk.Button(button_frame, text="Opción 3", command=self.opcion1)

        button1.grid(row=0, column=0, padx=10, pady=10)
        button2.grid(row=0, column=1, padx=10, pady=10)
        button3.grid(row=0, column=2, padx=10, pady=10)

    def opcion1(self):
        """Método que pasa a la ventana principal y destruye la ventana del menú"""
        self.app.entrada_ca(self.usuario)
        self.destroy()
