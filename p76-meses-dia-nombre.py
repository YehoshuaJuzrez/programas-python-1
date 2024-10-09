#• Leer un número de mes (ej 4).
#• Imprimir: días del mes, y nombre del mes (ej marzo, 30).
#• Asume 28 para febrero, guarda días en una lista, y nombres de mes en otra.

import os; os.system("cls")

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mes = int(input("Introduce un número de mes (1-12): "))

if 1 <= mes <= 12:
    
    nombre_mes = meses[mes - 1]
    dias_mes = dias[mes - 1]
    
    print(f"El mes de {nombre_mes} tiene {dias_mes} días.")
else:
    print("Número de mes inválido. Por favor, introduce un número entre 1 y 12.")