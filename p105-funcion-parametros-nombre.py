# Funciones con nombres en todos los parametros

import os

def saluda(apaterno, amaterno, nombre):
    print(f'Hola {apaterno} {amaterno} {nombre}')

# principal
os.system('clear')
saluda('Castañeda', 'Ramirez', 'Carlos')
saluda(nombre='Carlos', amaterno='Ramirez', apaterno='Castañeda')
saluda(amaterno='Bernal', nombre='Rocio', apaterno='Soto')