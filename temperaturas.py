import random

# Definir dimensiones
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4

# Crear matriz 3D con temperaturas aleatorias entre 10 y 35 grados
matriz_temperaturas = [[[random.randint(10, 35) for _ in range(7)] for _ in range(semanas)] for _ in range(len(ciudades))]

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
else:
    print("Selección inválida. Intente de nuevo.")
