# Conversiones a Pesos
import os; os.system("clear")
# Definir diccionario de conversiones de monedas

conversiones = {
'USD': 20.50, # Dólar estadounidense
'EUR': 22.30, # Euro
'GBP': 25.80, # Libra esterlina
'JPY': 0.19, # Yen japonés
'CAD': 16.20 # Dólar canadiense
}

print("Conversor de monedas a pesos mexicanos")

# Mostrar opciones de monedas
print("\nOpciones de monedas: ")
for moneda in conversiones:
    print(f"- {moneda} ")
# Solicitar moneda y cantidad
while True:
    moneda = input("\nIngrese la moneda a convertir: ").upper()
    if moneda in conversiones: break
cantidad = float(input("Ingrese la cantidad a convertir: "))
# Realizar conversión
resultado = cantidad * conversiones[moneda]
print(f"{cantidad:,.2f} {moneda} son {resultado:,.2f} MXN")