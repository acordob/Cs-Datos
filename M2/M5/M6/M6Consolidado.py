# EVALUACIÓN FINAL M6: ANÁLISIS DEL IMPACTO DEL CAMBIO CLIMÁTICO EN LA PRODUCCIÓN AGRÍCOLA
# Alumna: Alejandra Córdoba Sepúlveda

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.linear_model import Ridge, Lasso


# Cargar los datos y exploración de los datos
df = pd.read_csv("cambio_climatico_agricultura.csv")

# Exploración
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Limpieza de datos
df.dropna(inplace=True)

# Visualización
# plt.figure(figsize=(10, 6))
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
sns.histplot(df['Temperatura_promedio'], kde=True)
plt.title('Distribución de Temperatura Promedio')

plt.subplot(2, 2, 2)
sns.histplot(df['Cambio_lluvias'], kde=True)
plt.title('Distribución de Cambio en Lluvias')

plt.subplot(2, 2, 3)
sns.histplot(df['Frecuencia_sequías'], kde=True)
plt.title('Distribución de Frecuencia de Sequías')

plt.subplot(2, 2, 4)
sns.histplot(df['Producción_alimentos'], kde=True)
plt.title('Distribución de Producción de Alimentos')

plt.tight_layout()
plt.show()

# Matriz de correlación
plt.figure(figsize=(8, 6))
correlation_matrix = df.drop('País', axis=1).corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Matriz de Correlación')
plt.show()

# Boxplots para detertar valores atípicos
plt.figure(figsize=(15, 8))
df_numeric = df.drop('País', axis=1)
df_numeric.boxplot()
plt.title('Detección de Valores Atípicos')
plt.xticks(rotation=45)
plt.show()

# Preprocesamiento y escalamiento de datos

X_reg = df[['Temperatura_promedio', 'Cambio_lluvias', 'Frecuencia_sequías']]
y_reg = df['Producción_alimentos']

X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

scaler_reg = StandardScaler()
X_train_scaled_reg = scaler_reg.fit_transform(X_train_reg)
X_test_scaled_reg = scaler_reg.transform(X_test_reg)


# Aplicación Modelo Regresión (opcional árbol de decisión o random forest)

model_reg = LinearRegression()
model_reg.fit(X_train_scaled_reg, y_train_reg)
y_pred_reg = model_reg.predict(X_test_scaled_reg)

print("MAE:", mean_absolute_error(y_test_reg, y_pred_reg))
print("MSE:", mean_squared_error(y_test_reg, y_pred_reg))
print("R²:", r2_score(y_test_reg, y_pred_reg))

# Aplicación Modelo Clasificación

def impacto(valor):
    if valor < 500000:
        return "Alto"
    elif valor < 850000:
        return "Medio"
    else:
        return "Bajo"

df["impacto"] = df["Producción_alimentos"].apply(impacto)

X_clf = df[["Temperatura_promedio", "Cambio_lluvias", "Frecuencia_sequías"]]
y_clf = df["impacto"]

X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(X_clf, y_clf, test_size=0.2, random_state=42)

scaler_clf = StandardScaler()
X_train_scaled_clf = scaler_clf.fit_transform(X_train_clf)
X_test_scaled_clf = scaler_clf.transform(X_test_clf)

print(f"Tamaño del conjunto entrenamiento (Regresión: {len(X_train_reg)})")
print(f"Tamaño del conjunto prueba (Regresión): {len(X_test_reg)})")
print(f"Tamaño del conjunto entrenamiento (Clasificación: {len(X_train_clf)})")
print(f"Tamaño del conjunto prueba (Clasificación): {len(X_test_clf)})")

# Entrenamiento y evaluación
model_clf = DecisionTreeClassifier()
model_clf.fit(X_train_scaled_clf, y_train_clf)
y_pred_clf = model_clf.predict(X_test_scaled_clf)

# Confusion matrix
cm = confusion_matrix(y_test_clf, y_pred_clf, labels=["Alto", "Medio", "Bajo"])
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=["Alto", "Medio", "Bajo"], yticklabels=["Alto", "Medio", "Bajo"])
plt.title('Matriz de Confusión')
plt.xlabel('Predicciones')
plt.ylabel('Valores Reales')
plt.show()

print(classification_report(y_test_clf, y_pred_clf))


# Optimización del modelo
# Regularización en regresión
ridge = Ridge()
lasso = Lasso(max_iter=10000)

# Validación cruzada
ridge_params = {'alpha': [0.1, 1, 10]}
lasso_params = {'alpha': [0.01, 0.1, 1]}

ridge_grid = GridSearchCV(ridge, ridge_params, cv=3)
lasso_grid = GridSearchCV(lasso, lasso_params, cv=3)

ridge_grid.fit(X_train_scaled_reg, y_train_reg)
lasso_grid.fit(X_train_scaled_reg, y_train_reg)

print("\nMejor Ridge:", ridge_grid.best_params_)
print("Mejor Lasso:", lasso_grid.best_params_)

# Análisis de resultados y conclusiones:
# Las variables influyen en la producción de alimentos en los distintos países.
# El modelo de regresión evidenció que el aumento de temperatura y la disminución de lluvias tienden a correlacionarse negativamente.
# El modelo de clasificación muestra zonas críticas de sequía.