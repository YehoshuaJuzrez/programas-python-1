#• Leer n nombres de ciudades en una lista hasta introducir $
#• Imprimir cuantos elementos son, y la lista completa
#• Ordenar la lista en orden descendente y mostrar (sort)
#• Imprimir cuantas ciudades inician con la letra consonante (startswith) y sus nombres

import os; os.system("cls")

ciudades = []
ciudad = ""

while ciudad != "$":
    ciudad = input("Ingresa el nombre de una ciudad (o $ para finalizar): ")
    if ciudad != "$":
        ciudades.append(ciudad)

print("\nCantidad de ciudades ingresadas:", len(ciudades))
print("Lista de ciudades:", ciudades)


ciudades.sort(reverse=True)
print("\nLista de ciudades en orden descendente:", ciudades)

consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
ciudades_consonantes = [ciudad for ciudad in ciudades if ciudad.startswith(tuple(consonantes))]

print("\nCantidad de ciudades que empiezan con consonante:", len(ciudades_consonantes))
print("Ciudades que empiezan con consonante:", ciudades_consonantes)