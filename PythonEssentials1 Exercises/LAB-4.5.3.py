"""
---
4.5.3 Ejemplos de funciones: Factoriales
---
La siguiente función a definir calcula factoriales. ¿Recuerdas cómo se calcula un factorial?

0! = 1 (¡Si!, es verdad)
1! = 1
2! = 1 * 2
3! = 1 * 2 * 3
4! = 1 * 2 * 3 * 4
:
:
n! = 1 * 2 * 3 * 4 * ... * n-1 * n

Se expresa con un signo de exclamación, y es igual al producto de todos los números naturales previos al argumento o número dado.

Escribamos el código. Creemos una función con el nombre factorial_function.
"""

def factorial(n):
    resultado = 1
    if n < 0:
        return None
    elif n < 2:
        return 1
    else:
        for i in range(2, n + 1):
            resultado *= i
        return resultado

n = int(input("De qué numero entero quieres obtener el factorial: "))
if factorial(n) == None:
    print("No se puede obtener factorial de numeros negativos")
else:
    print(n, "! = ", factorial(n))
