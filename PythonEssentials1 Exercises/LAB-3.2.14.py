"""
---
3.2.14   LAB   Fundamentos del bucle while
---
 
Escenario
Escucha esta historia: Un niño y su padre, un programador de computadoras, juegan con bloques de madera. Están construyendo una pirámide.

Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide - es plana. La pirámide se apila de acuerdo con un principio simple: cada capa inferior contiene un bloque más que la capa superior.


La figura ilustra la regla utilizada por los constructores:



Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede construir utilizando estos bloques.

Nota: La altura se mide por el número de capas completas - si los constructores no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.

Prueba tu código con los datos que hemos proporcionado.
"""

blocks = int(input("Ingresa el número de bloques: "))
height = 1
used_blocks = blocks
if blocks == 1:
    print("La altura es ", height)
else:
    height = 2
    used_blocks -= 1
    for block in range(2, blocks + 1):
        if used_blocks - height >= 0:
            used_blocks = used_blocks - height
            height += 1
        else:
            height -= 1
            break
            
print("La altura de la pirámide:", height)
