"""
Este programa en Python toma una lista de nombres y construye parejas aleatorias, asegurándose de que nadie quede solo. En caso de que la cantidad de nombres sea impar, se crea un grupo de tres personas.
"""
import random

nombres = ['Juan', 'Ana', 'Luis', 'Maria', 'Pedro', 'Sofia', 'Juana']
random.shuffle(nombres)
if len(nombres) % 2 == 0:
    for i in range(0, len(nombres), 2):
        print(nombres[i], "y", nombres[i+1])
else:
    for i in range(0, len(nombres)-3, 2):
        print(nombres[i], "y", nombres[i+1])
    print(nombres[-3], ",", nombres[-2], "y", nombres[-1])