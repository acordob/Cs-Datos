import numpy as np

# Conjunto de datos de ejemplo
datos = [3, 5, 7, 9, 11]

# Calcular la varianza poblacional (sin corrección)
varianza_poblacional = np.var(datos) # Para población

# Calcular la varianza muestral (con corrección de Bessel)
varianza_muestral = np.var(datos, ddof=1) # Para muestra con corrección de Bessel

# Imprimir los resultados
print("Varianza poblacional:", varianza_poblacional)
print("Varianza muestral:", varianza_muestral)