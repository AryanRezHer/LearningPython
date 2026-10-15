"""
---
2.6.9   LAB   Entradas y salidas simples
---

Escenario
Tu tarea es completar el código para evaluar los resultados de cuatro operaciones aritméticas básicas.

Los resultados deben imprimirse en la consola.

Es posible que no puedas proteger el código de un usuario que quiera dividir entre cero. Está bien, no te preocupes por eso por ahora.

Prueba tu código - ¿produce los resultados esperados?

No te mostraremos ningún dato de prueba - eso sería demasiado simple.

"""

a = float(input("Introduce un valor para la variable a: "))
b = float(input("Introduce un valor para la variable b: "))

suma = a + b
print("La suma de los dos numeros es: ", suma)

resta = a - b
print("La resta de los dos numeros es: ", resta)

multiplicacion = a * b
print("La multiplicacion de los dos numeros es: ", multiplicacion)

division = a / b
print("La division de los dos numeros es: ", division)
