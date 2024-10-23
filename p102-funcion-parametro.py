# funcion con parametros

import os

def saluda(nombre):
    print(f'Hola {nombre} bienvenido a python, tu nombre tiene {len(nombre)} caracteres')


# programa principal
os.system('clear')
saluda('Carlos Castañeda')
saluda('Juan Perez Diaz')
saluda('Maria Soto Garcia')