"""Fichero que contiene la ventana para el registro de usuarios"""
import tkinter as tk
from tkinter import messagebox

class VentanaRegistro(tk.Toplevel):
    """Clase que configura la ventana para realizar el registro de usuario"""
    def __init__(self, app, registro):
        super().__init__(app)
        self.app = app
        self.title("Registro de usuario")
        self.geometry("300x150")

        self.registro = registro

        self.interfaz()

    def interfaz(self):
        """Método que configura la interfaz de la ventana"""
        #Texto
        self.texto_usuario = tk.Label(self, text="Nombre de usuario: ")
        self.texto_contrasena = tk.Label(self, text="Introduce una contraseña:")
        #Cuadros
        self.cuadro_usuario = tk.Entry(self)
        self.cuadro_contrasena = tk.Entry(self, show="*")
        #Botones
        self.boton_registro = tk.Button(self, text="Registrarse", command=self.registrar_usuario)
        self.boton_inicio = tk.Button(self, text="Volver al inicio de sesión", command=self.app.abrir_inicio_sesion)

        #Posicionamos los elementos
        self.texto_usuario.pack()
        self.cuadro_usuario.pack()
        self.texto_contrasena.pack()
        self.cuadro_contrasena.pack()
        self.boton_registro.pack()
        self.boton_inicio.pack()

    def registrar_usuario(self):
        """Método asociado al botón para registrar al usuario"""
        #Almacenamos los datos introducidos por el usuario
        usuario = self.cuadro_usuario.get()
        contrasena = self.cuadro_contrasena.get()

        #Comprobamos que no exista el usuario
        if self.registro.agregar_usuario(usuario, contrasena):
            messagebox.showinfo("Éxito", "Se ha registrado correctamente al usuario")
            self.app.abrir_inicio_sesion()
            self.destroy() #Salimos de la ventana
        else:
            messagebox.showerror("Error", "El usuario ya existe")
