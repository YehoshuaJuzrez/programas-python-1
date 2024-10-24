## Usar funciones

import p124_funciones as m
import os

nums = [1,5,7,9,13,15,17]

os.system('clear')
print(f'El mayor es = ', m.mayor(nums))
print(f'El menor es = ', m.menor(nums))
print(f'El promedio es = ', m.promedio(nums))

print(m.pi)
print(m.gt)