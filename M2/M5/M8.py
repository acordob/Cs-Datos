# EVALUACIÓN FINAL M8: PREDICCIÓN DE NATALIDAD SEGÚN FACTORES SOCIOECONÓMICOS
# Alumna: Alejandra Córdoba Sepúlveda

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Carga y Exploración de Datos
df = pd.read_csv("dataset_natalidad.csv")

# Estadísticas descriptivas
print(df.head())
print(df.describe())
print(df.isnull().sum())

# Visualización
# Mapa de Correlaciones
plt.figure(figsize=(10, 8))
# Exclude the 'País' column before calculating correlation
sns.heatmap(df.drop('País', axis=1).corr(), annot=True, cmap="coolwarm")
plt.title("Correlación entre variables")
plt.show()

# Variables predictoras y objetivo
X = df.drop(columns=["País", "Tasa_Natalidad"])
y = df["Tasa_Natalidad"]

# Escalado
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# División en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Definición del modelo
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.2),
    Dense(32, activation='relu'),
    Dense(1, activation='linear')  # Regresión
])

# Compilación
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              loss='mean_squared_error',
              metrics=['mae'])

# Entrenamiento
history = model.fit(X_train, y_train, epochs=100, validation_split=0.2, verbose=1)

plt.plot(history.history['loss'], label='Entrenamiento')
plt.plot(history.history['val_loss'], label='Validación')
plt.title("Pérdida durante el entrenamiento")
plt.xlabel("Épocas")
plt.ylabel("MSE")
plt.legend()
plt.show()

# Predicciones
y_pred = model.predict(X_test).flatten()

# Métricas
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"RMSE: {rmse:.2f}")
print(f"R²: {r2:.2f}")

# Importancia aproximada por pesos absolutos de la primera capa
weights = model.layers[0].get_weights()[0]
importancia = np.mean(np.abs(weights), axis=1)

# Mostrar importancia
for i, col in enumerate(X.columns):
    print(f"{col}: {importancia[i]:.4f}")

# Visualizar predicciones vs valores reales
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], linestyle='--', color='red')
plt.xlabel("Valores reales")
plt.ylabel("Predicciones")
plt.title("Predicciones vs Valores reales")
plt.show()

# Análisis y Resultados
# Variables mas influyentes: PIB_per_capita, Nivel_Educativo y Acceso_Salud.
# Relaciona los resultados con tendencias demográficas globales: El PIB muestra una correlación negativa con la tasa de natalidad, lo que epxlica que en paises más desarrollados exista una baja natalidad.
# Propón mejoras o ajustes para futuras versiones del modelo: se podría ampliar la muestra para hacer el modelo mas preciso.