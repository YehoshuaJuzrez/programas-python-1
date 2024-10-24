# Utilizar funciones contenidas en modulos de la biblioteca estandar de python
import os
import datetime, calendar, platform

os.system('clear')
print(f'\nSistema operativo: \n{platform.system()} {platform.release()}')
print(f'\nDirectorio actual: \n{os.getcwd()}')

print(f'\nListado de archivos en el directorio raíz:')
os.chdir('/')
print(os.listdir())
print('\nVariables de entorno:')
for key, value in os.environ.items():
    print(f'{key}: {value}')
print(f"\nRuta de ejecución: \n{os.getenv('PATH')}")

# Algunas funciones del modulo datetime
ahora = datetime.datetime.now()
print('\nLa fecha y hora actuales: ', ahora)
print('\nLa fecha actual: ', ahora.strftime('%b / %d / %Y'))
print('\nLa hora actual: ', ahora.strftime('%H:%M'))

#Algunas funciones del modulo calendar
print('\nCalendario 2024: \n')
calendar.prcal(2024)
print('\nMes abril 2024: \n')
calendar.prmonth(2024,4)

diractual = "D:\Computacion_Aplicada\programas-python"
os.mkdir(diractual+'/la_carpeta_que_acabo_de_crear')
print(diractual)