import tkinter as tk
from tkinter import ttk

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #Creamos una instancia de la clase ttk.Label y se la asignamos a una variable etiqueta1.
        self.etiqueta_celsius = ttk.Label(
            parent, text="Temperatura en ºC:")
        #Posicionamos la etiqueta en la ventana
        self.etiqueta_celsius.place(x=20, y=20)

        #Añadimos la caja de texto con ttk.Entry()
        self.caja_celsius = ttk.Entry(parent)
        self.caja_celsius.place(x=140, y=20, width=60)

        #Añadimos el boton con ttk.Button y le asociamos la función de convertir
        self.boton_conversion = ttk.Button(parent, text="Convertir",
                                           command=self.convertir_temp)
        self.boton_conversion.place(x=20, y=60)

        #Añadimos la etiqueta de Kelvin
        self.etiqueta_kelvin = ttk.Label(
            parent, text="Temperatura en K: n/a")
        self.etiqueta_kelvin.place(x=20, y=120)

        #Añadimos la etiqueta de Fahrenheit
        self.etiqueta_fahrenheit = ttk.Label(
            parent, text="Temperatura en ºF: n/a")
        self.etiqueta_fahrenheit.place(x=20, y=160)

    def convertir_temp(self):
        """Función que coge la temperatura introducida en la caja de ºC y
        la pasa a K y ªF"""
        #Cogemos la temperatura de la caja
        temp_celsius = float(self.caja_celsius.get())
        temp_kelvin = temp_celsius + 273.15
        temp_fahrenheit = temp_celsius*1.8 + 32

        #Reescribimos la etiqueta de K con la nueva temperatura
        self.etiqueta_kelvin.config(
            text=f"Temperatura en K: {temp_kelvin}")

        # Reescribimos la etiqueta de ºF con la nueva temperatura
        self.etiqueta_fahrenheit.config(
            text=f"Temperatura en ºF: {temp_fahrenheit}")


if __name__ == '__main__':
    #Creamos la raíz
    root = tk.Tk()
    #Le damos un titulo al programa
    root.title("Conversor de temperatura")
    #Le damos un tamaño al programa
    root.config(width=400, height=300)

    app = App(root)

    #Ejecuta el programa principal
    root.mainloop()
