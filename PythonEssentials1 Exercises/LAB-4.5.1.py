"""
4.5.1 - Cálculo IMC
"""

def imc(peso, altura):
    if altura < 1.0 or altura > 2.5 or peso < 20 or peso > 200:
        return None
    else:
        IMC = peso / altura ** 2
        return IMC
    
peso = float(input("Introduce tu peso en KG: "))
altura = float(input("Introduce tu altura en metros: "))
print(imc(peso, altura))
