# EVALUACIÓN FINAL M9: ANÁLISIS DE MOVIMIENTOS MIGRATORIOS CON SPARK
# Alumna: Alejandra Córdoba Sepúlveda

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.ml.feature import VectorAssembler, StringIndexer
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Crear sesión Spark
spark = SparkSession.builder.appName("Migraciones").getOrCreate()

# Cargar dataset
df = spark.read.csv("migraciones.csv", header=True, inferSchema=True)

# Convertir a RDD
rdd = df.rdd

# Exploración y estadísticas descriptivas
df.show(5)
df.printSchema()
df.describe().show()

# Transformar a rdd y DataFrame
# Ejemplo: filtrar migraciones por causa económica
rdd_economica = rdd.filter(lambda x: x["Causa"] == "Económica")

# Mapear países de destino
destinos = rdd.map(lambda x: x["País_Destino"])

# Contar registros
print("Total de migraciones:", rdd.count())
print("Migraciones económicas:", rdd_economica.count())
print("Primeros destinos:", destinos.take(5))

# Filtrar por año reciente
df_filtrado = df.filter(df["Año"] >= 2015)

# Agregación: migraciones por país de destino
df_agg = df.groupBy("País_Destino").count().orderBy("count", ascending=False)
df_agg.show()

# Guardar en formato Parquet
df_agg.write.parquet("resultados_migracion.parquet")


# Registrar tabla temporal
df.createOrReplaceTempView("migraciones")

# Países con mayor recepción
spark.sql("""
SELECT País_Destino, COUNT(*) AS Total
FROM migraciones
GROUP BY País_Destino
ORDER BY Total DESC
""").show()

# Razones de migración por región
spark.sql("""
SELECT Región_Origen, Causa, COUNT(*) AS Total
FROM migraciones
GROUP BY Región_Origen, Causa
ORDER BY Total DESC
""").show()

# Indexar variables categóricas
indexer = StringIndexer(inputCol="Causa", outputCol="Causa_Index")
df_indexed = indexer.fit(df).transform(df)

# Vector de características
assembler = VectorAssembler(
    inputCols=["Ingreso_Origen", "Ingreso_Destino", "Tasa_Desempleo", "Causa_Index"],
    outputCol="features"
)
df_final = assembler.transform(df_indexed).select("features", "Migró")  # Migró: 1 si migró, 0 si no

# División de datos
train, test = df_final.randomSplit([0.8, 0.2], seed=42)

lr = LogisticRegression(labelCol="Migró", featuresCol="features")
modelo = lr.fit(train)

# Evaluación
predicciones = modelo.transform(test)
evaluator = BinaryClassificationEvaluator(labelCol="Migró")
precision = evaluator.evaluate(predicciones)

print(f"Precisión del modelo: {precision:.2f}")

