# Generar dos listas de numeros aleatorios, elevarlas al cuadrado y sumarlas en una tercera

import os, random; os. system('Clear')

listaA = []
listaB= []
listaC= []

n = int(input('Cuantos elementos : '))


print('Generando aleatorios....')
for x in range(n):
    listaA.append(random.randint(1,10))
    listaB.append(random.randint(1,10))

print('listaA = ', listaA)
print('listaB = ', listaB)
print()

for x in range(n):
    listaA[x]= listaA[x] * listaA[x]
    listaB[x]= listaB[x] * listaB[x]
    listaC.append(listaA[x] + listaB[x])


print('listaA =', listaA)
print()
print('listaB =', listaB)
print()
print('listaC =', listaC)