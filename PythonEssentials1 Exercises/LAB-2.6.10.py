"""
---
2.6.10   LAB   Operadores y expresiones
---

Escenario
Tu tarea es completar el código para poder evaluar la siguiente expresión:

Expresión matemática

El resultado debe de ser asignado a y. Se cauteloso, observa los operadores y priorízalos. Utiliza cuantos paréntesis sean necesarios.

Puedes utilizar variables adicionales para acortar la expresión (sin embargo, no es muy necesario). Prueba tu código cuidadosamente.
"""

x = float(input("Ingresa un valor: "))

y = 1/(x + 1/(x + 1/(x + 1/x)))

print("El resultado de la expresion matemática es: ", y)
