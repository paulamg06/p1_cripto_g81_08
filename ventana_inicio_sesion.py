"""Fichero que contiene la clase de la ventana del inicio de sesión"""
import tkinter as tk
from tkinter import messagebox

class VentanaInicioSesion(tk.Toplevel):
    """Clase que contiene la ventana para que los usuarios inicien sesión"""
    def __init__(self, app, registro):
        super().__init__(app)
        self.app = app
        self.title("Inicio de sesión")
        self.geometry("300x150")
        self.interfaz()

        self.registro = registro

    def interfaz(self):
        """Método que contiene los textos, cuadros y botones de la ventanta"""
        #Apartado del usuario
        self.usuario = tk.Label(self, text="Usuario: ")
        self.usuario.pack()
        self.cuadro_usuario = tk.Entry(self)
        self.cuadro_usuario.pack()

        #Apartado de la contraseña
        self.contrasena_label = tk.Label(self, text="Contraseña: ")
        self.contrasena_label.pack()
        self.cuadro_contrasena = tk.Entry(self, show="*") #Ocultamos la contraseña
        self.cuadro_contrasena.pack()

        #Boton de inicio
        self.boton_inicio = tk.Button(self, text="Iniciar sesión", command=self.iniciar_sesion)
        self.boton_inicio.pack()

        #Boton de registro
        self.boton_registro = tk.Button(self, text="Registrar usuario", command=self.registrar_usuario)
        self.boton_registro.pack()

    def iniciar_sesion(self):
        """Método que comprueba que la contraseña sea correcta"""
        usuario = self.cuadro_usuario.get()
        contrasena = self.cuadro_contrasena.get()

        #Inicio de sesión correcto
        if self.registro.verificar_credenciales(usuario, contrasena):
            messagebox.showinfo("Inicio de sesión correcto", "Bienvenido, " + usuario)
            #Guardamos el usuario
            self.app.usuario = usuario
            #Pasamos a la siguiente ventana
            self.app.abrir_menu_principal()
            self.destroy()

        else:
            messagebox.showerror("Inicio de sesión incorrecto", "Usuario y/o contraseña no válido/s")

    def registrar_usuario(self):
        """Método que abre la ventana para registrar el usuario"""
        self.app.abrir_registro_usuario()
        self.destroy()
