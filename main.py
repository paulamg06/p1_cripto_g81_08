"""Fichero que corre la aplicación"""
import tkinter as tk
from aplicacion import Aplicacion

#Creamos la raíz
root = tk.Tk()
db_file = "sqllite"

app = Aplicacion(root, db_file)

#Ejecuta el programa principal
root.mainloop()