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

# Visualización
plt.figure(figsize=(10, 6))
sns.pairplot(df.drop(columns='País'))
plt.suptitle("Distribución de variables climáticas y producción", y=1.02)
plt.show()

# Boxplots para detertar valores atípicos
fig, axs = plt.subplots(1, 4, figsize=(20, 5))
for i, col in enumerate(df.columns[1:]):
    sns.boxplot(df[col], ax=axs[i])
    axs[i].set_title(f'Boxplot de {col}')
plt.tight_layout()
plt.show()

# Preprocesamiento y escalamiento de datos

X_reg = df[["Temperatura_promedio", "Cambio_lluvias", "Frecuencia_sequías"]]
y_reg = df["Producción_alimentos"]

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

df["impacto"] = pd.qcut(df["Producción_alimentos"], q=3, labels=["Bajo", "Medio", "Alto"])
X_clf = df.drop(["impacto", "País", "Producción_alimentos"], axis=1) # Corrected to drop 'País' as well
y_clf = df["impacto"]

# Split the data *after* creating the 'impacto' column
X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(X_clf, y_clf, test_size=0.2, random_state=42)

# Scale the data *after* splitting
scaler_clf = StandardScaler()
X_train_scaled_clf = scaler_clf.fit_transform(X_train_clf)
X_test_scaled_clf = scaler_clf.transform(X_test_clf)

# Entrenamiento y evaluación
model_clf = DecisionTreeClassifier()
model_clf.fit(X_train_scaled_clf, y_train_clf)
y_pred_clf = model_clf.predict(X_test_scaled_clf)

print(confusion_matrix(y_test_clf, y_pred_clf))
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

ridge_grid.fit(X_train_reg, y_train_reg)
lasso_grid.fit(X_train_reg, y_train_reg)

print("\nMejor Ridge:", ridge_grid.best_params_)
print("Mejor Lasso:", lasso_grid.best_params_)

# Análisis de resultados y conclusiones
# Las variables influyen en la producción de alimentos en los distintos países.
# El modelo de regresión evidenció que el aumento de temperatura y la disminución de lluvias tienden a correlacionarse negativamente.
# El modelo de clasificación muestra zonas críticas de sequía.