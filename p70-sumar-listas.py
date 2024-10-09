# Sumar dos listas de numeros introducidas por el usuario

import os; os.system('Clear')

c = int(input('Cuantos elementos ?'))

lista1 = []
lista2 = []
lista3 = []

print ('Leer lista1')
for i in range(lista3) :
    n = int (input(f"lista1[{i}]="))
    lista1.append(n)
print(lista1)

print ('Leer lista2')
for i in range(lista3) :
    n = int (input(f"lista2[{i}]="))
    lista2.append(n)
print(lista2)

print ('Suma de listas lista3 = lista1 + lista2')
for i in range(lista3):
    lista3.append(lista1[i] * lista2[i])
print(lista3)