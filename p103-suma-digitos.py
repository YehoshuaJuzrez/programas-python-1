# funcion que recibe dos parametros

import os

def saluda(apaterno, nombre):
    print(f'Hola {apaterno} {nombre} longitud {len(apaterno+nombre)}')


# principal
os.system('clear')
saluda('Castañeda', 'Carlos')
#saluda('Soto')
#saluda('Soto', 'Bernal', 'Rocio')