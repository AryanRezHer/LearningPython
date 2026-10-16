"""
---
3.1.11   LAB   Fundamentos de la sentencia if-else
---

Escenario
Érase una vez una tierra de leche y miel - habitada por gente feliz y próspera. La gente pagaba impuestos, por supuesto - su felicidad tenía límites. El impuesto más importante, denominado Impuesto Personal de Ingresos (IPI, para abreviar) tenía que pagarse una vez al año y se evaluó utilizando la siguiente regla:

si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual al 18% del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal).
si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 2 centavos, más el 32% del excedente sobre 85,528 pesos.
Tu tarea es escribir una calculadora de impuestos.

Debe aceptar un valor de punto flotante: el ingreso.
A continuación, debe imprimir el impuesto calculado, redondeado a pesos totales. Hay una función llamada round() que hará el redondeo por ti - la encontrarás en el código de esqueleto del editor.
Nota: este país feliz nunca devuelve dinero a sus ciudadanos. Si el impuesto calculado es menor que cero, solo significa que no hay impuesto (el impuesto es igual a cero). Ten esto en cuenta durante tus cálculos.

Observa el código en el editor - solo lee un valor de entrada y genera un resultado, por lo que debes completarlo con algunos cálculos inteligentes.

Prueba tu código con los datos que hemos proporcionado.
"""

ingresos = float(input("Cuantos ingresos en pesos tienes anuales: "))

if ingresos <= 85528:
    ipi = ingresos * 0.18 - 556.2
    if ipi <= 0:
        ipi = 0
else:
    ipi = (ingresos - 85528) * 0.32 + 14839.2

print("El impuesto calculado del sueldo: ", ingresos, "es de: ", round(ipi,0))
