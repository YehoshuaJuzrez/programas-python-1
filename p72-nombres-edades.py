# Procesa nombres y edades en dos listas paralela, usuario introduce los datos 

import os; os.system('Clear')

nombres = []
edades = []

while True:
    nombre = input ('Nombres :')
    if nombre!= '*':
        nombres.append(nombre)
        edad = int(input ('Edad :'))
        edades.append(edades)
    else:
        break

print('Nombres :', nombres)
print('Edades :', edades)

print('Mayoresd de edad : ')
for i in range(len(nombres)):
    if edades[i] >= 18:
        print(f'Nombre = {nombres[i]}, Edad = {edades[i]}')


pos = edades.index(max(edades))
print(f'El alumno {nombres[pos]}, con edad de {edades[pos]} es el mayor de todos')