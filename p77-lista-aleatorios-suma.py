#• Generar 2 listas de 10 números aleatorios
#• Suma ambas listas en una tercera, suma solo los elementos de cada lista si ambos son impares
#• Imprime las 3 listas

import os; os.system("cls")
import random

lista1 = [random.randint(1, 100) for _ in range(10)]
lista2 = [random.randint(1, 100) for _ in range(10)]

suma_impares = []

for i in range(10):
    if lista1[i] % 2 != 0 and lista2[i] % 2 != 0:
        suma_impares.append(lista1[i] + lista2[i])
    else:
        suma_impares.append(0)  

print("Lista 1: ", lista1)
print("Lista 2: ", lista2)
print("Suma de impares: ", suma_impares)