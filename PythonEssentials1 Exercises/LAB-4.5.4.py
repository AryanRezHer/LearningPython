"""
---
4.5.4 Números Fibonacci
---
¿Estás familiarizado con la serie Fibonacci?

Son una secuencia de números enteros los cuales siguen una regla sencilla:

el primer elemento de la secuencia es igual a uno (Fib1 = 1)
el segundo elemento también es igual a uno (Fib2 = 1)
cada número después de ellos son la suman de los dos números anteriores (Fibi = Fibi-1 + Fibi-2)
Aquí están algunos de los primeros números en la serie Fibonacci:

fib_1 = 1 fib_2 = 1 fib_3 = 1 + 1 = 2 fib_4 = 1 + 2 = 3 fib_5 = 2 + 3 = 5 fib_6 = 3 + 5 = 8 fib_7 = 5 + 8 = 13
"""

def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        resultado = Fibonacci(n - 2) + Fibonacci(n - 1)
        return resultado

while True:
    number = int(input("Introduce un numero entero para obtener su valor en la serie Fibonacci: "))
    if number > 0:
        break


for i in range(1, number + 1):
    resultado = Fibonacci(i)
    print("Fib", i, "=", resultado)
