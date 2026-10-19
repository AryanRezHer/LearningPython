"""
---
4.3.6   LAB   Día del año: escribiendo y usando tus propias funciones
---

Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) y devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.

Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos de prueba al código. Esta prueba es solo el comienzo.
"""
def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    month_31_days = [1, 3, 5, 7, 8, 10, 12]
    month_30_days = [4, 6, 9, 11]
    bisiesto = is_year_leap(year)
    if month > 0 and month < 13:
        if bisiesto:
            if month in month_31_days:
                return 31
            elif month in month_30_days:
                return 30
            else:
                return 29
        else:
            if month in month_31_days:
                return 31
            elif month in month_30_days:
                return 30
            else:
                return 28
    else:
        return None

def day_of_year(year, month, day):
    total_days = 0
    for i in range(1, month):
        total_days += days_in_month(year, i)
    total_days += day
    return total_days  

print(day_of_year(2000, 12, 31))
