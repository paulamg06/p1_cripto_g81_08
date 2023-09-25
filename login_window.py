"""Fichero que contiene la clase de la ventana del inicio de sesión"""
import tkinter as tk
from tkinter import messagebox

class LoginWindow(tk.Toplevel):
    """Clase que contiene la ventana para que los usuarios inicien sesión"""
    def __init__(self, app):
        super().__init__(app)
        self.app = app
        self.title("Inicio de sesión")
        self.geometry("300x150")
        self.interfaz()

    def interfaz(self):
        """Método que contiene los textos, cuadros y botones de la ventanta"""
        #Apartado del usuario
        self.usuario = tk.Label(self, text="Usuario: ")
        self.usuario.pack()
        self.cuadro_usuario = tk.Entry(self)
        self.cuadro_usuario.pack()

        #Apartado de la contraseña
        self.contraseña_label = tk.Label(self, text="Contraseña: ")
        self.contraseña_label.pack()
        self.cuadro_contraseña = tk.Entry(self, show="*") #Ocultamos la contraseña
        self.cuadro_contraseña.pack()

        #Boton de inicio
        self.boton_inicio = tk.Button(self, text="Iniciar sesión", command=self.comprobar_contraseña)
        self.boton_inicio.pack()

    def comprobar_contraseña(self):
        """Método que comprueba que la contraseña sea correcta"""
        usuario = self.cuadro_usuario.get()
        contraseña = self.cuadro_contraseña.get()

        #Inicio de sesión correcto
        if usuario == "1234" and contraseña == "1234":
            messagebox.showinfo("Inicio de sesión correcto", "Bienvenido, " + usuario)
            #Pasamos a la siguiente ventana
            self.app.entrada_app(usuario)
            self.destroy()

        else:
            messagebox.showerror("Inicio de sesión incorrecto", "Usuario y/o contraseña no válido/s")
