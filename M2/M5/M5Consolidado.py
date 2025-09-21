# EVALUACIÓN FINAL M5: DISEÑO Y ANÁLISIS DE EXPERIMENTO SOBRE EL RENDIMIENTO ACADÉMICO
# Alumna: Alejandra Córdoba Sepúlveda

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
from scipy.stats import ttest_ind, t

grupo_A = np.array([85, 90, 78 ,88 ,92, 80, 86, 89, 84, 87, 91, 82, 83, 85, 88]) # Grupo tutoría
grupo_B = np.array([70, 72, 75, 78, 80, 68, 74, 76, 79, 77, 73, 71, 75, 78, 80]) # Grupo control

# Diseño de Experimento: explica brevemente cómo se podría mejorar el diseño del experimento para reducir posibles sesgos
# - Muestreo Aleatoro: Asignar aleatoriamente a los estudiantes.
# - Tamaño de la muestra: Aumentar el tamaño para mejorar la potencia estadística.
# - Aplicar Muestreo Estratificado: diviendo la población en subgrupos.

# Cálculo de la media y desviación estándar
media_A = np.mean(grupo_A)
std_A = np.std(grupo_A, ddof=1)

media_B = np.mean(grupo_B)
std_B = np.std(grupo_B, ddof=1)

print(f"Grupo A - Media: {media_A: .2f}, Desviación estándar: {std_A: .2f}")
print(f"Grupo B - Media: {media_B: .2f}, Desviación estándar: {std_B: .2f}")

# Visualización con Histogramas o diagramas de cajas - Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(data=[grupo_A, grupo_B], palette="pastel")
plt.xticks([0, 1], ["Grupo A (Tutoría)", "Grupo B (Control)"])
plt.title("Distribución de Calificaciones")
plt.ylabel("Puntaje")
plt.show()

# Prueba de Hipótesis
# H0 NULA: No hay diferencia en el rendimiento académico entre los grupos
# #H1 ALTERNATIVA: El grupo con tutoría tiene mejor rendimiento

t_stat, p_valor = stats.ttest_ind(grupo_A, grupo_B, alternative='greater')

print("--- Prueba de Hpótesis: \n H0 Nula: No hay diferencia en el rendimiento entre los grupos, \n H1 Alternativa: El grupo con tutoría tiene mejor rendimiento  \n Nivel de significancia p>0.05 ---")
print(f"Estadístico t = {t_stat: .3f}, Valor_p = {p_valor: .3f}")

if p_valor < 0.05:
    print("Interpretación: Existe evidencia significativa que la tutoría tiene efecto positivo: Se rechaza la hipótesis Nula H0")
else:
    print("No se rechaza H0: No hay evidencia suficiente para afirmar que la tutoría mejora el rendimiento")


# Cálculo de Intervalo de Confianza del 95%
# Parámetros
diff_media = media_A - media_B # Diferencia de Medias

 # Error estándar de la diferencia
se_diff = np.sqrt((std_A**2 / len(grupo_A)) + (std_B**2 / len(grupo_B)))

# Grados de libertad
df = len(grupo_A) + len(grupo_B) - 2

# Valor crítico t para 95% de confianza
t_crit = stats.t.ppf(0.975, df)

# Intervalo de confianza
lim_inferior = diff_media - t_crit * se_diff
lim_superior = diff_media + t_crit * se_diff

print(f"Diferencia de medias: {diff_media: .2f}")
print(f"Itervalo de confianza 95%: ({lim_inferior: .2f}, {lim_superior: .2f})")

# Iterpretación: Si el intervalo no incluye 0, hay evidencia de diferencia significativa
# El análisis sugiere que el grupo con tutoría obtuvo mejores resultados
# La prueba t y el intervalo de confianza respaldan la hipótesis alternativa
# Se recomienda implementar el programa de tutoría como estrategia educativa