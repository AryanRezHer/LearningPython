"""
---
4.5.2 Ejemplos de funciones: Triángulos
---

Ahora trabajaremos con triángulos. Comenzaremos con una función que verifique si tres lados de ciertas longitudes pueden formar un triángulo.

En la escuela aprendimos que la suma arbitraria de dos lados tiene que ser mayor que la longitud del tercer lado.

No será algo difícil. La función tendrá tres parámetros - uno para cada lado.

Regresará True si todos los lados pueden formar un triángulo, y False de lo contrario. En este caso, is_a_triangle es un buen nombre para dicha función.

Observa el código en el editor. Ahí se encuentra la función. Ejecuta el programa.
"""

def is_a_triangle(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False



a = float(input("Introduce un valor para el lado A del triangulo: "))
b = float(input("Introduce un valor para el lado B del triangulo: "))
c = float(input("Introduce un valor para el lado C del triangulo: "))
if is_a_triangle(a,b,c):
    print("Es un triangulo")
else:
    print("No es posible crear un triangulo")
