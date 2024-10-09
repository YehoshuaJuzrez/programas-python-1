#• Llenar una lista con los primeros n números impares (ej 1 3 5 7 9 11 n)
#• Calcular e imprimir la suma y promedio de los números
#• Mostrar los números que son divisibles entre 3 y sumarlos
#• Pedir un elemento a buscar en la lista original y decir si esta y en que posición

import os; os.system("cls")

def primeros_impares(n):
    impares = []
    num = 1
    while len(impares) < n:
        impares.append(num)
        num += 2
    return impares

n = int(input("Ingresa la cantidad de números impares que deseas generar: "))
impares = primeros_impares(n)

suma_total = sum(impares)
promedio = suma_total / len(impares)

divisibles_entre_3 = [num for num in impares if num % 3 == 0]
suma_divisibles_entre_3 = sum(divisibles_entre_3)

print("\nLista de los primeros", n, "números impares:", impares)
print("Suma total de los números impares:", suma_total)
print("Promedio de los números impares:", promedio)
print("Números divisibles entre 3:", divisibles_entre_3)
print("Suma de los números divisibles entre 3:", suma_divisibles_entre_3)


elemento = int(input("\nIngresa el número que deseas buscar en la lista: "))

if elemento in impares:
    posicion = impares.index(elemento)
    print(f"El número {elemento} está en la lista en la posición {posicion}.")
else:
    print(f"El número {elemento} no está en la lista.")