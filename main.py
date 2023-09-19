"""Fichero que corre la aplicación"""
import tkinter as tk
from aplicacion import Aplicacion

#Creamos la raíz
root = tk.Tk()

#Le damos un titulo al programa
root.title("Cuenta atras")

#Le damos un tamaño al programa
root.config(width=600, height=500)

app = Aplicacion(root)

#Ejecuta el programa principal
root.mainloop()