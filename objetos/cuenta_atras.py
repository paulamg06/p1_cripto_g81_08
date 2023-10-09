"""Fichero que guarda las unidades de la cuenta atras"""

class CuentaAtras:
    def __init__(self, years, days, hours, minutes):
        self.years = years
        self.days = days
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        # Si los años no es None, entonces imprimimos que queda +years años
        if self.years:
            return "+" + str(self.years) + " años."

        # En caso contrario
        return str(self.days) + "días, " + str(self.hours) + " horas, " + str(self.minutes) + " minutos."