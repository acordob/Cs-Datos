# DataPro Solution - Funciones cálculos matemáticos
# Alumna: Alejandra Córdoba Sepúlveda
# Fecha:

# Importación de módulos
import math
import random
import statistics


# Crea una función calcular_area_rectangulo que reciba dos parámetros (largo y ancho) y retorne el área del rectángulo (1 punto).
def calcular_area_rectangulo(largo, ancho):
    return largo * ancho
area = calcular_area_rectangulo(7,5) # Ejemplo
print(f"El área del rectangulo es: {area}")

# Crea una función calcular_circunferencia que reciba el radio de un círculo y retorne su circunferencia. Usa la constante pi del módulo math (2 puntos).
def calcular_circunferencia(radio):
    return 2 * math.pi * radio
circulo = calcular_circunferencia(5)
print(f"La circunferencia del circulo es de: {circulo: 2f}")

# Crea una función calcular_promedio que reciba una lista de números y retorne el promedio (1 punto)
def calcular_promedio(lista_numeros):
    if not lista_numeros:
        return 0
    return sum(lista_numeros) / len(lista_numeros)

lista =[1, 2, 3, 4, 5, 6, 7, 10]

promedio = calcular_promedio(lista)
print(f"El promedio de números es de: {promedio: 2f} ")

# Importa la función mean del módulo statistics y úsala en una nueva función calcular_promedio_avanzado para calcular el promedio de la misma lista de números del punto anterior (2 puntos).
def calcular_promedio_avanzado(lista_numeros):
    return statistics.mean(lista_numeros)
promedio_avanzado = calcular_promedio_avanzado(lista)
print(f"El promedio avanzado de números es de: {promedio_avanzado: 2f} ")

# Crea una función generar_numeros_aleatorios que reciba dos parámetros (cantidad y limite), y retorne una lista de números aleatorios entre 1 y el límite especificado. Usa el módulo random (2 puntos).
def generar_numeros_aleatorios(cantidad, limite):
    return [random.randint(1, limite) for _ in range(cantidad)]
numero = generar_numeros_aleatorios(5, 100)
print(f"Número aleatorio: {numero}")

# Escribe un programa que utilice cada una de las funciones anteriores e imprime los resultados de cada cálculo (2 puntos).
if __name__ == "__main__":
    print("** Cálculos generados para DataPro Solutions **\n")

    # Área de rectángulo
    largo = 5
    ancho = 3
    area = calcular_area_rectangulo(largo, ancho)
    print(f"Área del rectángulo ({largo}x{ancho}): {area}")

    # Circunferencia
    radio = 4
    circunferencia = calcular_circunferencia(radio)
    print(f"Circunferencia de radio {radio}: {circunferencia:.2f}")

    # Promedios
    notas = [85, 90, 78, 92]
    promedio_simple = calcular_promedio(notas)
    promedio_avanzado = calcular_promedio_avanzado(notas)
    print(f"Promedio simple: {promedio_simple:.2f}")
    print(f"Promedio avanzado: {promedio_avanzado:.2f}")

    # Números aleatorios
    aleatorios = generar_numeros_aleatorios(5, 100)
    print(f"Números aleatorios generados: {aleatorios}")