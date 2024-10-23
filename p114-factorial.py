# funcion factorial

import os

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

# Principal
os.system('clear')
n = int(input('Dame un numero entero y te regreso su factorial: '))
print('\nEl factorial de ', n, 'es ', factorial(n))