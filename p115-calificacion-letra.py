# Procesa un promedio y regresa una calificacion con letra y un mensaje 

import os

def calificacion(cal):
    if cal >=90 and cal<100:
        return 'A', 'Excelente'
    if cal >=80 and cal<90:
        return 'B', 'Bien'
    if cal >=70 and cal<80:
        return 'C', 'Suficiente'
    if cal >=60 and cal<70:
        return 'D', 'Deficiente'
    elif cal >=0 and cal<60:
        return 'F', 'Reprobado'

# Principal
os.system('clear')
cal = int(input('Calificacion entre 1 y 100 ? '))
letra, mensaje = calificacion(cal)
print(f'Tu calificacion de {cal} corresponde a la letra {letra} y esta {mensaje}')