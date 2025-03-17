import random

# Función para calcular la temperatura promedio
def calcular_temperatura_promedio(datos):
    """
    Calcula la temperatura promedio de una ciudad durante un período de tiempo.

    :param datos: Un diccionario donde las claves son nombres de ciudades y los valores son diccionarios
                  con las semanas como claves y listas de temperaturas como valores.
    :return: Un diccionario con las ciudades como claves y las temperaturas promedio como valores.
    """
    promedios = {}

    for ciudad, semanas in datos.items():
        total_temperaturas = 0
        total_dias = 0

        for semana, temperaturas in semanas.items():
            total_temperaturas += sum(temperaturas)
            total_dias += len(temperaturas)

        if total_dias > 0:
            promedios[ciudad] = total_temperaturas / total_dias
        else:
            promedios[ciudad] = 0  # Si no hay datos, el promedio es 0

    return promedios

# Definir dimensiones
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4

# Crear matriz 3D con temperaturas aleatorias entre 10 y 35 grados
matriz_temperaturas = [[[random.randint(10, 35) for _ in range(7)] for _ in range(semanas)] for _ in range(len(ciudades))]

# Convertir la matriz 3D en un diccionario de diccionarios
datos_temperaturas = {}
for idx, ciudad in enumerate(ciudades):
    datos_temperaturas[ciudad] = {}
    for semana in range(semanas):
        datos_temperaturas[ciudad][f"Semana{semana + 1}"] = matriz_temperaturas[idx][semana]

# Pedir al usuario que seleccione una ciudad
print("Ciudades disponibles:")
for idx, ciudad in enumerate(ciudades, 1):
    print(f"{idx}. {ciudad}")

opcion = int(input("Seleccione el número de la ciudad que desea ver: ")) - 1

if 0 <= opcion < len(ciudades):
    ciudad_seleccionada = ciudades[opcion]
    print(f"\nTemperaturas para {ciudad_seleccionada}:")
    for semana in range(semanas):
        print(f"  Semana {semana + 1}:")
        for dia, temp in zip(dias, matriz_temperaturas[opcion][semana]):
            print(f"    {dia}: {temp}°C")
    
    # Calcular y mostrar el promedio de temperaturas por semana
    print(f"\nPromedio de temperaturas para {ciudad_seleccionada}:")
    for semana in range(semanas):
        suma_temperaturas = sum(matriz_temperaturas[opcion][semana])
        promedio = suma_temperaturas / len(dias)
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")
    
    # Calcular el promedio general de la ciudad seleccionada usando la función
    promedio_general = calcular_temperatura_promedio({ciudad_seleccionada: datos_temperaturas[ciudad_seleccionada]})
    print(f"\nPromedio general de temperaturas para {ciudad_seleccionada}: {promedio_general[ciudad_seleccionada]:.2f}°C")
else:
    print("Selección inválida. Intente de nuevo.")
