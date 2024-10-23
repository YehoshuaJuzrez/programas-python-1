# Temperaturas

def farenheit(temp):
    return (temp * (9/5)) + 32

def centigrados(temp):
    return (temp - 32) * (5/9)

while True:
    print('[ 1 ] Convertir a Farenheit')
    print('[ 2 ] Convertir a Centigrados')
    op = int(input("Elige ? "))
    
    if op == 1:
        temp = float(input('Dame una temperatura en Centigrados? '))
        print(f'La temperatura en grados Farenheit es {farenheit(temp):.2f}')
        break

    elif op == 2:
        temp = float(input('Dame una temperatura en Farenheit? '))
        print(f'La temperatura en grados Centigrados es {centigrados(temp):.2f}')
        break

    else:
        print("Opción no válida, por favor intenta de nuevo.")