"""Fichero que guarda las unidades de la cuenta atras"""

class CuentaAtras:
    def __init__(self, years, months, days, hours, minutes):
        self.years = years
        self.months = months
        self.days = days
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return str(self.years) + " años, " + str(self.months) + " meses, " + str(self.days) + " días. " + str(self.hours) + ":" + str(self.minutes)