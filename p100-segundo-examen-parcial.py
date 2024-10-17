# Se desea procesar los empleados de una empresa de muebles

empleados = []

def obtener_datos_empleado():
    # Obtener nombre
    nombre = input("Introduce el nombre del empleado: ")

    # Obtener edad
    while True:
        try:
            edad = int(input("Introduce la edad del empleado: "))
            if edad <= 0:
                print("Edad inválida. Debe ser un número mayor que 0.")
            else:
                break
        except ValueError:
            print("Por favor, ingresa un número válido para la edad.")

    # Obtener sexo
    while True:
        sexo = input("Introduce el sexo del empleado (h/m): ").lower()
        if sexo not in ('h', 'm'):
            print("Agregar variable válida (h/m).")
        else:
            break

    # Obtener sueldo
    while True:
        try:
            sueldo = float(input("Introduce el sueldo del empleado: "))
            if sueldo <= 0:
                print("Sueldo inválido. Debe ser un número mayor que 0.")
            else:
                break
        except ValueError:
            print("Por favor, ingresa un número válido para el sueldo.")

    # Obtener pasatiempos
    while True:
        pasatiempos = input("Introduce los pasatiempos del empleado: ")
        if not pasatiempos:
            print("Agregar variable válida.")
        else:
            break

    return {
        "nombre": nombre,
        "edad": edad,
        "sexo": sexo,
        "sueldo": sueldo,
        "pasatiempos": pasatiempos
    }

# Bucle principal para agregar empleados
while True:
    empleado = obtener_datos_empleado()
    empleados.append(empleado)

    continuar = input("¿Deseas agregar otro empleado? (s/n): ")
    if continuar.lower() != 's':
        break

# Imprimir lista de empleados
print("\nLista de Empleados:")
print(empleados)

print("\nTabla de datos:")
print("Nombre\tEdad\tSexo\tSueldo\tPasatiempos")
for emp in empleados:
    print(f"{emp['nombre']}\t{emp['edad']}\t{emp['sexo']}\t{emp['sueldo']}\t{emp['pasatiempos']}")

# Resumen de datos
total_empleados = len(empleados)
total_hombres = sum(1 for x in empleados if x['sexo'] == 'h')
total_mujeres = sum(1 for x in empleados if x['sexo'] == 'm')
suma_edad = sum(x['edad'] for x in empleados)
promedio_edad = suma_edad / total_empleados if total_empleados > 0 else 0
suma_sueldo = sum(x['sueldo'] for x in empleados)
promedio_sueldo = suma_sueldo / total_empleados if total_empleados > 0 else 0

empleado_mayor_edad = max(empleados, key=lambda x: x['edad'])
empleado_menor_edad = min(empleados, key=lambda x: x['edad'])

# Imprimir resumen
print("\nResumen")
print(f"Total de empleados: {total_empleados}")
print(f"Hombres: {total_hombres}")
print(f"Mujeres: {total_mujeres}")
print(f"Suma de edades: {suma_edad}")
print(f"Promedio de edad: {promedio_edad:.2f}")
print(f"Suma de sueldos: {suma_sueldo}")
print(f"Promedio de sueldo: {promedio_sueldo:.2f}")
print(f"\nEmpleado de mayor edad: {empleado_mayor_edad['nombre']} con {empleado_mayor_edad['edad']} años")
print(f"Empleado de menor edad: {empleado_menor_edad['nombre']} con {empleado_menor_edad['edad']} años")
