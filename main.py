"""Fichero que corre la aplicación"""
import tkinter as tk
from aplicacion import Aplicacion

#Creamos la raíz
root = tk.Tk()

app = Aplicacion(root)

#Ejecuta el programa principal
root.mainloop()