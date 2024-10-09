# Conversiones a metro

import os; os.system("clear")

# Definir diccionario de conversiones
conversiones = {
'km': 1000, # kilómetros a metros
'm': 1, # metros
'cm': 0.01, # centímetros a metros
'mm': 0.001 # milímetros a metros
}

longitud = int(input("Dame la longitud ?"))
while True:
    unidad = input("Unidad (km, m, cm ,mm ? ")
    if unidad in conversiones:
        break

resultado = longitud * conversiones[unidad]
print(f"{longitud:,.2f} {unidad} son {resultado:,.2f} metros")